import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import altair as alt
from PIL import Image



st.title(":male-student: Professional Integration of Master's Students  In Universities :female-student:")
st.sidebar.title(":male-technologist: Credits :writing_hand:")
st.sidebar.markdown("Name: Nathanaël RAKOTO")
st.sidebar.markdown("Class: BIA2")
st.sidebar.markdown("Linkedin: [Nathanaël RAKOTO](www.linkedin.com/in/nathanael-rakoto)")
st.sidebar.markdown("Github: [Nathanaël RAKOTO](https://github.com/Clutchboyyyy)")
st.sidebar.markdown("#datavz2023efrei")

#Erreur de certification :
#URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:997)>
#csv_url = "https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-insertion_professionnelle-master/download?format=csv"
#@st.cache
#def load_data():
    #data = pd.read_csv(csv_url, sep=';')
    #return data
#data = load_data()


#Chargement du dataset en Local alors
data = pd.read_csv("insertion_professionnelle.csv", sep=";")
#st.table(data.head(5))


#----------------------------------------------------------------------------------------------------

#Nettoyage de données
data = data.drop(columns=["etablissementactuel","remarque", "salaire_net_mensuel_regional_1er_quartile", "salaire_net_mensuel_regional_3eme_quartile", "id_paysage", "code_de_l_academie", "code_du_domaine", "diplome", "cle_etab", "cle_disc", "code_de_la_discipline"])
data = data[(data["taux_dinsertion"] != "ns") & (data["taux_dinsertion"] != "nd") & (data["taux_dinsertion"] != "fe")]
data['taux_dinsertion'] = data['taux_dinsertion'].astype(float)
data['taux_dinsertion'] = pd.to_numeric(data['taux_dinsertion'])
data = data[(data["taux_de_chomage_regional"] != "ns") & (data["taux_de_chomage_regional"] != "nd") & (data["taux_de_chomage_regional"] != "fe") & (data["taux_de_chomage_regional"] != ".")]
data = data.dropna(subset=["taux_de_chomage_regional"])
data['taux_de_chomage_regional'] = data['taux_de_chomage_regional'].astype(float)
data['taux_de_chomage_regional'] = pd.to_numeric(data['taux_de_chomage_regional'])
data = data[(data["emplois_stables"] != "ns") & (data["emplois_stables"] != "nd") & (data["emplois_stables"] != "fe") & (data["emplois_stables"] != ".")]
data = data.dropna(subset=["emplois_stables"])
data['emplois_stables'] = data['emplois_stables'].astype(float)
data['emplois_stables'] = pd.to_numeric(data['emplois_stables'])
data = data[(data["femmes"] != "ns") & (data["femmes"] != "nd") & (data["femmes"] != "fe") & (data["femmes"] != ".")]
data = data.dropna(subset=["femmes"])
data['femmes'] = data['femmes'].astype(float)
data['femmes'] = pd.to_numeric(data['femmes'])
data = data[(data["salaire_net_median_des_emplois_a_temps_plein"] != "ns") & (data["salaire_net_median_des_emplois_a_temps_plein"] != "nd") & (data["salaire_net_median_des_emplois_a_temps_plein"] != "fe") & (data["salaire_net_median_des_emplois_a_temps_plein"] != ".")]
data = data.dropna(subset=["salaire_net_median_des_emplois_a_temps_plein"])
data['salaire_net_median_des_emplois_a_temps_plein'] = data['salaire_net_median_des_emplois_a_temps_plein'].astype(float)
data['salaire_net_median_des_emplois_a_temps_plein'] = pd.to_numeric(data['salaire_net_median_des_emplois_a_temps_plein'])
data = data[(data["emplois_cadre"] != "ns") & (data["emplois_cadre"] != "nd") & (data["emplois_cadre"] != "fe") & (data["emplois_cadre"] != ".")]
data = data.dropna(subset=["emplois_cadre"])
data['emplois_cadre'] = data['emplois_cadre'].astype(float)
data['emplois_cadre'] = pd.to_numeric(data['emplois_cadre'])
#----------------------------------------------------------------------------------------------------

with st.container():
    st.write("You are a student or just someone who is concerned about his future, and you may be wondering what you want to do in the future once you've graduated, in what field, in what profession, in what company and possibly for what salary. Through this website, I'm going to help you think about this, so that you can choose what you really like, taking into account the different factors that I'm going to talk about.")
    st.write("\nTo help you make your choice, I'll use this dataset : ")
    st.write(data)
    st.write("This dataset has been constructed from information based on data collected as part of the national operation to collect data on the professional integration of Master's graduates over several years (from 2010 to 2019).")

    #------------------------------------------------------------------------------------------------
    #First part

    st.header(":male-office-worker: What can you expect when you graduate from university? :female-office-worker:")

    st.write("First of all, you may be wondering which field recruits the most university graduates. Here's an overview of the hiring rate in the 4 main fields.")
    plt.figure(figsize=(18, 6))
    sns.barplot(x=data["domaine"], y=data["taux_dinsertion"],palette="hls")
    plt.xlabel("Domaine")
    plt.ylabel("Taux d'insertion")
    st.pyplot(plt.gcf(), clear_figure=True)
    st.write("The graph shows that, overall, the 4 main fields of study have a hiring rate of more than 80%. However, education field seems to have the highest hiring rate, with over 98%. This very high rate could be explained by the shortage of teaching staff and the need to recruit in this area. Please note that this graph is based on an average of data from 2010 to 2019.")

    st.write("If you want to take a closer look at a particular year to get a more detailed view, here is a graph produced by the Ministry of National Education, Higher Education and Research during a survey on the professional integration of university graduates in 2010.")
    st.markdown("""
    <iframe 
      src="https://publication.enseignementsup-recherche.gouv.fr/eesr/7/illustration-EESR7_ES_21-1-insertion_des_diplomes_2010_de_master_selon_le_domaine_de_formation.php"
      height="500px" 
      width="100%">
    </iframe>  
    """, unsafe_allow_html=True)
    st.write("Unfortunately, this graph does not include data for the teaching sector. However, we can clearly see from this graph that in 2010, 2 fields were recruiting more than the others, Law-Economy-Management and Science-Technology-Health, and that they tended to have a higher percentage of stable jobs than the others (around 80%) and a higher net monthly salary, particularly as they have more people in full-time jobs (97%) than the other fields.")

    st.write("\nLet's now look at the distribution of Master's graduates by type of employer in that same year, according to their discipline :")
    st.markdown("""
        <iframe 
          src="https://publication.enseignementsup-recherche.gouv.fr/eesr/7/illustration-EESR7_ES_21-2-repartition_des_diplomes_2010_de_master_par_type_d_employeur_selon_la_discipline_en.php"
          height="500px" 
          width="100%">
        </iframe>  
        """, unsafe_allow_html=True)
    st.write("On this graph, we can see that the majority of master's graduates in 2010 were working in private companies, except for those with a master's degree in History-Geography who were predominantly working in the public sector as they aspired to become teachers. A trend seems to be emerging, as master's graduates are not leaning towards public enterprises and associations. However, those in the field of psychology do not hesitate to join associations, particularly in assisting others (25%).")

    st.write("Returning to our dataset, it would now be interesting to analyze the insertion rate according to the different disciplines, to get a more precise idea of the field you are doing and would like to do in the future.")
    sns.set_theme(style="whitegrid")
    f, ax = plt.subplots(figsize=(15, 20))
    sns.set_color_codes("pastel")
    sns.barplot(x="taux_dinsertion", y="discipline", data=data,
                label="Total", color="b")
    sns.set_color_codes("muted")
    sns.barplot(x="emplois_stables", y="discipline", data=data,
                label="Pourcentage d'emplois stables (CDI)", color="b")
    ax.legend(ncol=2, loc="lower left")
    ax.set(ylabel="",
           xlabel="Taux d'insertion")
    sns.despine(left=True, bottom=True)
    st.pyplot(f)
    st.write("This graph shows the proportion of stable jobs (permanent contracts) in the hiring rate for each discipline. Here we can see that Master's degrees in education and computer science have the highest hiring rate and the highest rate of stable employment, closely followed by Master's degrees in engineering and management. So these are the masters in which you're most likely to get a permanent contract. On the other hand, masters such as History-Geography or Humanities and Social Sciences have a lower rate of stable employment than the others, probably due to the flexibility of their work.")

    st.write("\nNow you may be interested to see in which region or city there's the most recruitment. Below are 2 maps of France, the first showing the cities with the highest hiring rates and vice versa, the second showing the cities where you're most likely to get a permanent contract.")
    coords = pd.read_csv('correspondance.csv', sep=";")
    df = pd.merge(data, coords, on='academie')
    fig = px.scatter_mapbox(df,
                            lat='lattitude', lon='longitude',
                            mapbox_style="carto-positron",
                            color='taux_dinsertion',
                            size='emplois_stables',
                            opacity=0.5,
                            title="🗺️ Taux d'insertion",
                            color_continuous_scale='solar')
    fig.update_layout(mapbox=dict(zoom=4))
    fig.update_layout(width=1000, height=700)
    st.plotly_chart(fig)
    st.write("On this map, we can see that the north-east of France is the region with the highest hiring rate. On the other hand, cities like Le Havre, Lyon, Grenoble and Monaco don't recruit as much as other regions.")

    fig = px.scatter_mapbox(df,
                            lat="lattitude",
                            lon="longitude",
                            color="emplois_stables",
                            size="taux_dinsertion",
                            size_max=20,
                            mapbox_style="carto-positron",
                            zoom=4,
                            title="🗺️ Taux d'emplois stables (CDI)",
                            color_continuous_scale='solar'
                            )
    fig.update_layout(width=1000, height=700)
    st.plotly_chart(fig)
    st.write("Here, we can see that cities like Lyon or Monaco, which don't recruit very much, justify this low percentage, as we can see that in these cities there is also a low rate of stable employment. So, these cities have a low hiring rate because they offer fewer permanent contracts than other cities.\n")


    st.write("\n\n\nMaybe you're a woman, and you'd like to know the proportion of women in each discipline to get an idea. Here's a graph that shows you how many of the new recruits are women.")
    sns.set_theme(style="whitegrid")
    f, ax = plt.subplots(figsize=(15, 15))
    sns.set_color_codes("pastel")
    sns.barplot(x="taux_dinsertion", y="discipline", data=data,
                label="Total", color="b")
    sns.set_color_codes("muted")
    sns.barplot(x="femmes", y="discipline", data=data,
                label="Pourcentage de femmes", color="b")
    ax.legend(ncol=2, loc="lower left")
    ax.set(ylabel="",
           xlabel="Taux d'insertion")
    sns.despine(left=True, bottom=True)
    st.pyplot(f)
    st.write("We can clearly see that the discipline with the most women is psychology, followed closely by primary education. On the other hand, the disciplines in which the percentage of women is still low compared to the others, but tending to increase from year to year, are computer science and engineering sciences. However, as I have shown previously, they are part of a rapidly evolving field, so get over these preconceived ideas and choose what you really like.")


    #------------------------------------------------------------------------------------------------------------
    #Second Part

    st.header(":money_with_wings: And what about the salary ? :money_mouth_face:")
    st.write("Like everyone, you are probably wondering how much you can expect to earn. In this section, I'll enlighten you on the subject.")
    st.write("\nLet's start by displaying the salary for each area to get an overall idea :")
    plt.figure(figsize=(18, 6))
    sns.barplot(x=data["domaine"], y=data["salaire_net_median_des_emplois_a_temps_plein"], estimator=lambda x: x.mean(), palette="hls")
    plt.xlabel("Domaine")
    plt.ylabel("Salaire mensuel net")
    st.pyplot(plt.gcf(), clear_figure=True)
    st.write("This graph shows the average net monthly salary for each major field. Here we can clearly see that 2 fields (Sciences, technologies and health | Law, economics and management) have a higher average salary than the others (~2000€).")

    st.write("\nLet's take a look at the evolution of this salary over the years :")
    alt.data_transformers.enable('default', max_rows=None)
    chart = alt.Chart(data).mark_line().encode(
        x='annee:N',
        y='mean(salaire_net_median_des_emplois_a_temps_plein):Q',
        color="domaine:N"
    ).properties(
          width=1000,
          height=700
        )
    st.altair_chart(chart)
    st.write("The salary difference I mentioned earlier is even more apparent here. Over the years, we can see that this difference has tended to increase more and more, reinforcing the idea that these 2 fields are growth areas. In contrast, the field of Letters, languages and art tends to stagnate at around €1,600. However, the teaching field seems to have seen its salary increase again over the last 2 years of the graph. You should keep an eye on the next evolution of this field.")


    sns.kdeplot(data=data, x="salaire_net_median_des_emplois_a_temps_plein", hue="domaine", shade=True,alpha=.5, common_norm=False)
    st.pyplot(plt.gcf(), clear_figure=True)
    st.write("Here's another way of visualizing this salary comparison between domains.")

    st.write("\nLooking at these graphs, you might wonder whether in these fields your salary can evolve with your years with the company. We're going to compare the salaries of Master's graduates with 18 months' experience with those with 30 months.")
    data_subset = data[["domaine", "situation", "salaire_net_median_des_emplois_a_temps_plein"]]
    grouped_data = data_subset.groupby(["domaine", "situation"]).mean().reset_index()
    dom = grouped_data["domaine"].unique()
    situation = grouped_data["situation"].unique()
    new_data = {}
    for attribute in situation:
        new_data[attribute] = grouped_data[grouped_data["situation"] == attribute]["salaire_net_median_des_emplois_a_temps_plein"].values
    x = np.arange(len(dom))
    width = 0.25
    multiplier = 0
    fig, ax = plt.subplots(figsize=(20, 10))
    for attribute, measurement in new_data.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_ylabel('Salaire net mensuel')
    ax.set_title('Salaire par domaine et situation')
    ax.set_xticks(x + width * (len(situation) - 1) / 2)
    ax.set_xticklabels(dom)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_ylim(0, grouped_data["salaire_net_median_des_emplois_a_temps_plein"].max() * 1.1)
    st.pyplot(plt.gcf(), clear_figure=True)
    st.write("We can see that most fields have a significant difference between 18 and 30 months, which shows that in these fields we can expect a certain salary evolution according to seniority in the company. On the other hand, the education field does not show this salary evolution.")

    st.write("To make things even clearer, let's take a look at this graph from Ministry of National Education, Higher Education and Research during a survey on the professional integration of university graduates in 2018 :")
    st.markdown("Acronyms Meanings :")
    st.markdown("- DEG: Law, economics and management")
    st.markdown("- LLA: Letters, languages, arts")
    st.markdown("- SHS: Humanities and Social Sciences")
    st.markdown("- STS: Sciences, technologies and health")
    image = Image.open('satisfaction.png')
    st.image(image)
    st.write("\nThe graph shows that the DEG and STS domains with the highest pay satisfaction also have the highest level fit. Otherwise, overall, all fields have a high level of satisfaction in terms of responsibilities and missions.")

    st.write("\nFinally, you know that salary varies according to the type of position held. Perhaps you'd like to become an executive, so let me show you this graph which gives an overview of the proportion of executive jobs for each discipline.")
    f, ax = plt.subplots(figsize=(15, 15))
    sns.set_color_codes("pastel")
    sns.barplot(x="taux_dinsertion", y="discipline", data=data,
                label="Total", color="b")
    sns.set_color_codes("muted")
    sns.barplot(x="emplois_cadre", y="discipline", data=data,
                label="Pourcentage d'emplois cadre", color="b")
    ax.legend(ncol=2, loc="lower left")
    ax.set(ylabel="",
           xlabel="Taux d'insertion")
    sns.despine(left=True, bottom=True)
    st.pyplot(f)
    st.write("The graph clearly shows that the disciplines with the most executive jobs are IT, engineering, psychology and education. If you want to get this type of job when you graduate from your Master's degree, don't hesitate, these are the disciplines you should maybe consider.")

    #--------------------------------------------------------------------------------------------
    #Last Part

    st.header(":star: Conclusion :star:")
    st.write("I hope that this shared reflexion has helped you for your orientation. We've looked at the different factors you need to take into account when making your decision, but the choice is entirely up to you. The future is yours, so choose what you really like.")
    st.write("\nThank you for reading !")

st.markdown("""
<style>
div.block-container{
   max-width: 85% !important;
   margin-left: auto; 
   margin-right: auto;
}
</style>  
""", unsafe_allow_html=True)
