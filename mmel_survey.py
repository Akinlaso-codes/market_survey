import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\USER\OneDrive\HUSSEIN\data_science-worldwuant_univerisity\market_survey.csv", encoding="cp1252")
print(df.info())
df[["lat", "lon"]] = (df["lat-lon"].str.split(",", expand=True)).astype(float)
df["state"] = df["location"].str.split(",", expand=True)[1]
df.info()
#df["company_name"] = df["customer_name"].str.replace("customer", "company")
#df.drop(columns= ["customer_name"], inplace=True)
#df.info()
#print(df["location"].str.split(""))
#df.to_csv(r"C:\Users\NGML\OneDrive\HUSSEIN\data_science-worldwuant_univerisity\martket_survey_clean.csv")
fig = px.scatter_mapbox(df,
    title="MAP SHOWING THE SPREAD OF IDENTIFIED COMPANIES ACROSS LAGOS, OGUN AND OYO STATE",
    lat="lat",
    lon="lon",
    zoom=7,
    color = df["gas_volume_mmscfd"],
    size = df["interest"],
    center={"lat": 7.376736, "lon": 3.939786},
    width=1200,
    height=650,
    hover_data=["company_name", "gas_volume_mmscfd", "location", "interest"],
)
                  
fig.update_layout(mapbox_style="open-street-map")
#fig.update_layout(hoverlabel_font_color="white")
#fig.update_layout(margin = {"r":10,"t":50,"l":10,"b":10})
fig.show()

#number_of_potential_customers_per_state = print(df["state"].value_counts().head(10))
#print(number_of_potential_customers_per_state)
#print(df["company_name"].groupby(df["state"]))

#print(df["state"].unique())
#state_counts = df["state"].value_counts()

print(df.state.value_counts())

fig, ax = plt.subplots()
           
df.state.value_counts().plot(kind='bar', ax=ax, color="red", xlabel="State Visited", ylabel="Number of Identified Companies", title="Number of Identified Companies Per State")

# to add horizontal gridlines behind bars in the plot

ax.set_axisbelow(True)

# to add horizontal gridlines
ax.grid(axis='y')

#ax.annotate(xy="df["state"].value_counts()")

plt.show()
           







#print(df.info())

#print(df.groupby("state")["company_name"].value_counts())

