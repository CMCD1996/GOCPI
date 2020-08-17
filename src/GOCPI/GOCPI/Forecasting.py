import os
import numpy as np
import pandas as pd


class Forecasting:
    def __unit__(self):
        """Initialises the forecasting class
        """
        self.forecasts = None

    def energy_balance_base(self, root, IEA_World_Energy_Balances_1,
                            IEA_World_Energy_Balances_Sheet_2, geography,
                            create_excel_spreadsheet):
        """[summary]

        Args:
            root ([type]): [description]
            IEA_World_Energy_Balances_1 ([type]): [description]
            IEA_World_Energy_Balances_Sheet_2 ([type]): [description]
            geography ([type]): [description]
            create_excel_spreadsheet ([type]): [description]

        Returns:
            (dataframe): Dataframe of base year energy balances based on selected geography
        """
        IEAWEBAK = root / IEA_World_Energy_Balances_1
        IEAWEBLZ = root / IEA_World_Energy_Balances_Sheet_2

        # Creates dataframes from IEA World Energy Statistics and Balances CSVs from Stats.OECD.org in the OECDiLibrary
        # Note the data is from #https:s//stats.oecd.org/ and #https://www-oecd-ilibrary-org.ezproxy.auckland.ac.nz/
        column_headers = [
            'ID', 'Unit', 'Geo_Code', 'Geo_Description', 'Prod_Code',
            'Prod_Description', 'Flow_Code', 'Flow_Description', 'Year',
            'Value(TJ)'
        ]
        f1 = open(IEAWEBAK, 'r')
        df_A = pd.read_csv(f1, header=None)
        df_A.columns = column_headers
        df_A.info(verbose=True)
        f2 = open(IEAWEBLZ, 'r')
        df_B = pd.read_csv(f2, header=None)
        df_B.columns = column_headers
        df_B.info(verbose=True)
        frames = [df_A, df_B]
        df = pd.concat(frames)
        df.info(verbose=True)

        # Closes the files
        f1.close()
        f2.close()

        # Find the unique items in each list of the energy balance sheets
        uv_prod = df.Prod_Description.unique()
        uv_geo = df.Geo_Description.unique()
        uv_flow = df.Flow_Description.unique()

        # Asks for an input
        Selected_Geo = input(
            "Please enter the geography you wish to extract energy balances")

        # Creates a pivot table to display the data in the way similar to the Energy Balance Sheet (cols = Energy Product, rows = Energy Flows)
        EBPT = pd.pivot_table(df,
                              index=['Geo_Description', 'Flow_Description'],
                              values=['Value(TJ)'],
                              columns=['Prod_Description'],
                              aggfunc=[np.sum],
                              fill_value=0)
        # Filters to the geography the user has selected
        Input_String = 'Geo_Description == ["' + Selected_Geo + '"]'
        EBPTG = EBPT.query(Input_String)

        if create_excel_spreadsheet == True:
            # Write the filtered pivot table to an excel file
            writer = pd.ExcelWriter(root / "Geo EB.xlsx")
            EBPTG.to_excel(writer, Selected_Geo)
            writer.save()

        # Returns the filtered pivot table as a dataframe
        return EBPTG