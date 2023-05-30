import numpy as np
from TP_PANDAS.exercices import df, df_city

# 1.
df["emissions"] = df.select_dtypes(include=[np.number]).sum(axis=1)
print(df)

# 2.
# jointure = df.merge(df_city, how="left", left_on="INSEE commune", right_on="CODGEO")
jointure = df.merge(df_city, how="left", left_on="INSEE commune", right_on="CODGEO")
# jointure = df.merge(df_city, how="left", left_index=True, right_index=True)

rd16_nan = jointure[jointure["LIBGEO"].isna()]["emissions"]
rd16_not_nan = jointure[~jointure["LIBGEO"].isna()]["emissions"]
print("="*30)
print(rd16_nan)
print("*"*30)
print(rd16_not_nan)

# 3.
print("*"*40)
inner_join  = df.merge(df_city, how="inner", left_on="INSEE commune", right_on="CODGEO")
print(inner_join)
print(inner_join.columns)
inner_join["empreinte_carbone"] = inner_join["emissions"] / inner_join["NBMENFISC16"]
print("="*50)
print(inner_join.dtypes)
print(inner_join[["CODGEO", "Commune", "empreinte_carbone"]])