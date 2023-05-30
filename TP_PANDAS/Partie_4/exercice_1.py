from ..utils.pandas_ressources import df

# 1.
df_wide = df.copy()
print(df_wide)

# 2.
# df_long = pandas.wide_to_long(df_wide, )
df_long = df_wide.melt(id_vars=["Commune", "INSEE commune"], var_name="Secteur", value_name="Emissions_CO2")
print(df_long)
df_sum = df_long.groupby("Secteur")["Emissions_CO2"].sum().sort_values(ascending=False)
print(df_sum)
# df_sum.plot(kind="bar")
# plt.title="Emission par secteur"
# plt.xlabel = "Secteur"
# plt.ylabel = "Total des emissions de CO2"
# plt.show()

df_sum_dep = df_long.loc[df_long.groupby("INSEE commune")["Emissions_CO2"].idxmax()]
print(df_sum_dep)

