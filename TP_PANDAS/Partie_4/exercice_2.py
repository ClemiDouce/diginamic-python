from ..utils.pandas_ressources import df

df_wide = df.copy()
print(df_wide)

df_long = df_wide.melt(id_vars=["Commune", "INSEE commune"], var_name="Secteur", value_name="Emissions_CO2")
print(df_long)

df_sum = df_long.groupby(["INSEE commune", "Secteur"])["Emissions_CO2"].sum().reset_index()
print(df_sum)

df_wide = df_long.pivot(index="Secteur", columns="INSEE commune", values="Emissions_CO2")
print(df_wide)

df_wide["Total_Emission"] = df_wide.sum(axis=0)
print(df_wide["Total_Emission"])