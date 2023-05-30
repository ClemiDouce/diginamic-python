import timeit
import os

import pandas as pd
from pynsee import download

df = pd.read_csv("https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert", sep=",")
df_city = download.download_file("FILOSOFI_COM_2016")

# I
# # 1.
# print(df.head(10))
#
# print(df.tail(15))
#
# print(df.sample(10))
#
# # 2.
# print(df.sample(frac=0.05))
#
# # 3.
# print(df.head(10).sample(100, replace=True))
#
# # 4.
# print(df.head(6).sample(100, replace=True, weights=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1]))
#
# # 5.
# print(df_city.head(6).sample(100, replace=True, weights=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1]))

# II
# 1.
# print(df.dtypes)
# print(df_city.dtypes)
#
df_city[df_city.columns[2:len(df_city.columns)]] = df_city[df_city.columns[2:len(df_city.columns)]].apply(pd.to_numeric)
# print(df_city.dtypes)
#
# # 2.
# print(df.shape)
# print(df_city.shape)
#
# # 3.
# print(df[["INSEE commune", "Commune"]].nunique())
# print(df_city[["CODGEO", "LIBGEO"]].nunique())

# # 4.
# x = df_city.groupby("LIBGEO").count()["CODGEO"]
# x = x[x > 1]
# x = x.reset_index()
# # print(x)
#
# # 5.
# observations = df_city[df_city["LIBGEO"].isin(x["LIBGEO"])]
#
# # 6.
# observations.loc[:, "LIBGEO"] = observations["LIBGEO"].str.normalize("NFKD")
# observations = observations.sort_values(by="LIBGEO", ascending=True)
# # print(observations)
#
# # 7.
# print(df_city[df_city['LIBGEO'].isin(x['LIBGEO'])]['NBPERSMENFISC16'].describe())
# print(df_city[~df_city['LIBGEO'].isin(x['LIBGEO'])]['NBPERSMENFISC16'].describe())
#
# # 8.
# grandes_villes = df_city[df_city["NBPERSMENFISC16"]>100000].copy()
# grandes_villes["duplication"] = grandes_villes["LIBGEO"].isin(x["LIBGEO"])
# print(grandes_villes["duplication"].mean())
#
# # 9.
# print(df_city[df_city.LIBGEO == 'Montreuil'])
# print(df_city[df_city.LIBGEO.str.contains('Saint-Denis')])

# III
# 1.

new_df = df.set_index("INSEE commune")
new_df_city = df_city.set_index("CODGEO")

# 2
new_df["departement"] = new_df.index.str[:2]
new_df_city["departement"] = new_df_city.index.str[:2]

# 3.
#
# df_log = new_df.groupby("departement").sum()
# # print(df_log[df_log.select_dtypes(include=[np.number])].apply(np.log))
# df_log = df_log.select_dtypes(include=[np.number]).apply(np.log)
# df_log.sample(5).plot(kind="bar", stacked=True)
# plt.xlabel("Departement")
# plt.ylabel("Emissions (log)")
# plt.title("Titre")
# plt.show()
# print(df_log.head(10))
# df_log.sample(5).plot(kind="bar")

# 4.
df_log_2 = new_df.groupby("departement").sum()
df_log_2["totalEmission"] = df_log_2.iloc[:, 1:-1].sum(axis=1)
df_log_2 = df_log_2.sort_values(by="totalEmission", ascending=False)
# print(df_log_2["totalEmission"])

top_10 = df_log_2.head(10)
bottom_5 = df_log_2.tail(5)

# IV
# 1.
df_copy = new_df.copy()
df_copy2 = new_df.copy()

df_copy.set_index("departement", inplace=True)
df_copy.reset_index(inplace=True)

# to_time = df_copy.drop("Commune", axis=1).groupby("departement")

# str_execution = 'df_copy["Routier"].sum()'
#
# # print(timeit.timeit(str_execution))
# # print(timeit.timeit(df_copy.drop("Commune", axis=1).groupby("departement").sum))

# IV
