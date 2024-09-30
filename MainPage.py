import streamlit as st
import pandas as pd
import psycopg2
import plotly as ply

import plotly.express as px



st.html("<h1 style=\"color:red;\">Welcome to Red Bus Transports</h1> ")
st.html("<h4 style=\"color:blue;\">Select the Government/Private bus Transport</h4> ")

col1, col2 = st.columns(2, vertical_alignment="bottom")

with col1:

    
   
    var=st.selectbox("Select", ["AGSRTC-ANDHRA PRADESH", "KSRTC-KERALA","TGRSC-TELEGANA",
                              "SBSTC-SOUTH BENGAL","HRTC-HIMACHAL","KTCL-KADAMBA",
                              "RSRTC-RAJASTHAN","ASTC-ASSAM","UPSRTC-UTTAR PRADESH","BSRTC-BIHAR","PRIVATE BUS TRANSPORT"])
   
    
st.html("<h5 style=\"color:green;\"> DETAILS- GOVT/PRIVATE bus that you have selected</h5> ")


if var =="AGSRTC-ANDHRA PRADESH":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus11;")


    with col2:

        a = st.selectbox("select the bus type",df)

  
   
    if a=='VENNELA (A.C. SLEEPER)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus11 where bustype= \'VENNELA (A.C. SLEEPER)\'")
        data = pd.DataFrame(df1)
    
        st.dataframe(data)
    if a=='SUPER LUXURY (NON-AC, 2 + 2 PUSH BACK)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus11 where bustype= \'SUPER LUXURY (NON-AC, 2 + 2 PUSH BACK)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Electric A/C Seater (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus11 where bustype= \'Electric A/C Seater (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus11 where bustype= \'A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    df1=conn.query("select bustype,avg(rating::float) over (partition by bustype ) as partitiontable from redbus11")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    a=[]
    for i in df1['partitiontable']:
        a.append(float(i))


    b=[]
    for i in df1['bustype']:
        b.append(i)


    fig = px.bar(df1, x="bustype", y="partitiontable",color='bustype',hover_name='partitiontable', title="Bus Ratings")


    st.plotly_chart(fig)

#################################

if var =="KSRTC-KERALA":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus2;")


    with col2:

        a = st.selectbox("select the bus type",df)
 
  
   
    if a=='Swift Deluxe Non AC Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus2 where bustype= \'Swift Deluxe Non AC Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='SWIFT-GARUDA A/C SEATER BUS':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus2 where bustype= \'SWIFT-GARUDA A/C SEATER BUS\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Super Express Non AC Seater Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus2 where bustype= \'Super Express Non AC Seater Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus2 where bustype= \'A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Seater / Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus2 where bustype= \'A/C Seater / Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Bharat Benz A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus2 where bustype= \'Bharat Benz A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='NON A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus2 where bustype= \'NON A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='VE A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus2 where bustype= \'VE A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='AC MULTI AXLE':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus2 where bustype= \'AC MULTI AXLE\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    df1=conn.query("select bustype,avg(rating::float) over (partition by bustype ) as partitiontable from redbus2")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    a=[]
    for i in df1['partitiontable']:
        a.append(float(i))


    b=[]
    for i in df1['bustype']:
        b.append(i)


    fig = px.bar(df1, x="bustype", y="partitiontable",color='bustype',hover_name='partitiontable', title="Bus Ratings")


    st.plotly_chart(fig)

    ######################

if var =="TGRSC-TELEGANA":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus3;")


    with col2:

        a = st.selectbox("select the bus type",df)

    if a=='Electric A/C Seater (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'Electric A/C Seater (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
  
   
    if a=='Swift Deluxe Non AC Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'Swift Deluxe Non AC Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='SWIFT-GARUDA A/C SEATER BUS':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'SWIFT-GARUDA A/C SEATER BUS\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Super Express Non AC Seater Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'Super Express Non AC Seater Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Seater / Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'A/C Seater / Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Bharat Benz A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'Bharat Benz A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='NON A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'NON A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='VE A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'VE A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='AC MULTI AXLE':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus3 where bustype= \'AC MULTI AXLE\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    df1=conn.query("select bustype,rating  from redbus3")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)

   
    #b=[]
    #for i in df1['bustype']:
    #    b.append(i)


    fig = px.bar(df1, x="bustype", y="rating",color='bustype',hover_name='rating', title="Bus Ratings")


    st.plotly_chart(fig)

##########

if var =="SBSTC-SOUTH BENGAL":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus4;")


    with col2:

        a = st.selectbox("select the bus type",df)
 
  
   
    if a=='Non AC Seater (2+3)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus4 where bustype= \'Non AC Seater (2+3)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Scania Multi-Axle AC Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus4 where bustype= \'Scania Multi-Axle AC Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Super Express Non AC Seater Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus4 where bustype= \'Super Express Non AC Seater Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus4 where bustype= \'A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='Volvo A/C Seater (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus4 where bustype= \'Volvo A/C Seater (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Bharat Benz A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus4 where bustype= \'Bharat Benz A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='NON A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus4 where bustype= \'NON A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='VE A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus4 where bustype= \'VE A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='Non A/C Seater / Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus4 where bustype= \'Non A/C Seater / Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    df1=conn.query("select bustype,avg(rating::float) over (partition by bustype ) as partitiontable from redbus4")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    a=[]
    for i in df1['partitiontable']:
        a.append(float(i))


    b=[]
    for i in df1['bustype']:
        b.append(i)


    fig = px.bar(df1, x="bustype", y="partitiontable",color='bustype',hover_name='partitiontable', title="Bus Ratings")


    st.plotly_chart(fig)

################

if var =="HRTC-HIMACHAL":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus5;")


    with col2:

        a = st.selectbox("select the bus type",df)
 
  
   
    if a=='Super Luxury Volvo AC Seater Pushback 2+2':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus5 where bustype= \'Super Luxury Volvo AC Seater Pushback 2+2\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Volvo A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus5 where bustype= \'Volvo A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Super Express Non AC Seater Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus5 where bustype= \'Super Express Non AC Seater Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='Scania Multi-Axle AC Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus5 where bustype= \'Scania Multi-Axle AC Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Seater / Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus5 where bustype= \'A/C Seater / Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Bharat Benz A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus5 where bustype= \'Bharat Benz A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='NON A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus5 where bustype= \'NON A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='VE A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus5 where bustype= \'VE A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='AC MULTI AXLE':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus5 where bustype= \'AC MULTI AXLE\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    df1=conn.query("select bustype,rating  from redbus5")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    


    b=[]
    for i in df1['bustype']:
        b.append(i)


    fig = px.bar(df1, x="bustype", y="rating",color='bustype',hover_name='bustype', title="Bus Ratings")


    st.plotly_chart(fig)

##############

if var =="KTCL-KADAMBA":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus6;")


    with col2:

        a = st.selectbox("select the bus type",df)
 
  
   
    if a=='Swift Deluxe Non AC Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus6 where bustype= \'Swift Deluxe Non AC Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Volvo Multi-Axle I-Shift A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus6 where bustype= \'Volvo Multi-Axle I-Shift A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Super Express Non AC Seater Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus6 where bustype= \'Super Express Non AC Seater Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus6 where bustype= \'A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Seater / Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus6 where bustype= \'A/C Seater / Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Bharat Benz A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus6 where bustype= \'Bharat Benz A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='NON A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus6 where bustype= \'NON A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='VE A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus6 where bustype= \'VE A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='AC MULTI AXLE':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus6 where bustype= \'AC MULTI AXLE\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    df1=conn.query("select bustype,rating  from redbus6")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    

    b=[]
    for i in df1['bustype']:
        b.append(i)


    fig = px.bar(df1, x="bustype", y="rating",color='bustype',hover_name='bustype', title="Bus Ratings")


    st.plotly_chart(fig)

################

if var =="RSRTC-RAJASTHAN":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus7;")


    with col2:

        a = st.selectbox("select the bus type",df)
 
  
   
    if a=='Swift Deluxe Non AC Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus7 where bustype= \'Swift Deluxe Non AC Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Express Non AC Seater 2+3':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus7 where bustype= \'Express Non AC Seater 2+3\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Deluxe AC Seater 2+2':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus7 where bustype= \'Deluxe AC Seater 2+2\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus7 where bustype= \'A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Seater / Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus7 where bustype= \'A/C Seater / Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Bharat Benz A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus7 where bustype= \'Bharat Benz A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='NON A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus7 where bustype= \'NON A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='VE A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus7 where bustype= \'VE A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='AC MULTI AXLE':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus7 where bustype= \'AC MULTI AXLE\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    df1=conn.query("select bustype,avg(rating::float) over (partition by bustype ) as partitiontable from redbus7")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    a=[]
    for i in df1['partitiontable']:
        a.append(float(i))


    b=[]
    for i in df1['bustype']:
        b.append(i)


    fig = px.bar(df1, x="bustype", y="partitiontable",color='bustype',hover_name='partitiontable', title="Bus Ratings")


    st.plotly_chart(fig)

##################

if var =="ASTC-ASSAM":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus8;")


    with col2:

        a = st.selectbox("select the bus type",df)
 
  
   
    if a=='Swift Deluxe Non AC Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus8 where bustype= \'Swift Deluxe Non AC Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Volvo AC Seater 2+2"':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus8 where bustype= \'Volvo AC Seater 2+2\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='A/C Seater Push Back (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus8 where bustype= \'A/C Seater Push Back (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus8 where bustype= \'A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Seater / Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus8 where bustype= \'A/C Seater / Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Bharat Benz A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus8 where bustype= \'Bharat Benz A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='NON A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus8 where bustype= \'NON A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='VE A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus8 where bustype= \'VE A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='AC MULTI AXLE':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus8 where bustype= \'AC MULTI AXLE\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    df1=conn.query("select bustype,avg(rating::float) over (partition by bustype ) as partitiontable from redbus8")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    a=[]
    for i in df1['partitiontable']:
        a.append(float(i))


    b=[]
    for i in df1['bustype']:
        b.append(i)


    fig = px.bar(df1, x="bustype", y="partitiontable",color='bustype',hover_name='partitiontable', title="Bus Ratings")


    st.plotly_chart(fig)

############

if var =="UPSRTC-UTTAR PRADESH":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus9;")


    with col2:

        a = st.selectbox("select the bus type",df)

    if a=='Ordinary Non AC Seater 2+3':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'Ordinary Non AC Seater 2+3\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='Janrath AC Seater 2+2':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'Janrath AC Seater 2+2\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
   
    if a=='Swift Deluxe Non AC Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'Swift Deluxe Non AC Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='SWIFT-GARUDA A/C SEATER BUS':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'SWIFT-GARUDA A/C SEATER BUS\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Janrath AC Seater 2+3':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'Janrath AC Seater 2+3\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Seater / Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'A/C Seater / Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Bharat Benz A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'Bharat Benz A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='NON A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'NON A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='VE A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'VE A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=="AshokLeyland Stile A/C":
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus9 where bustype= \'AshokLeyland Stile A/C\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    df1=conn.query("select bustype,avg(rating::float) over (partition by bustype ) as partitiontable from redbus9")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    a=[]
    for i in df1['partitiontable']:
        a.append(float(i))


    b=[]
    for i in df1['bustype']:
        b.append(i)


    fig = px.bar(df1, x="bustype", y="partitiontable",color='bustype',hover_name='partitiontable', title="Bus Ratings")


    st.plotly_chart(fig)

###################

if var =="BSRTC-BIHAR":

    conn = st.connection("postgresql", type="sql")

    df = conn.query("SELECT bustype FROM redbus10;")


    with col2:

        a = st.selectbox("select the bus type",df)
 
  
   
    if a=='Swift Deluxe Non AC Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus10 where bustype= \'Swift Deluxe Non AC Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='SWIFT-GARUDA A/C SEATER BUS':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus10 where bustype= \'SWIFT-GARUDA A/C SEATER BUS\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Super Express Non AC Seater Air Bus (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus10 where bustype= \'Super Express Non AC Seater Air Bus (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus10 where bustype= \'A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='A/C Seater / Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus10 where bustype= \'A/C Seater / Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='Bharat Benz A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus10 where bustype= \'Bharat Benz A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='NON A/C Semi Sleeper (2+2)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus10 where bustype= \'NON A/C Semi Sleeper (2+2)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    if a=='VE A/C Sleeper (2+1)':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus10 where bustype= \'VE A/C Sleeper (2+1)\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)

    if a=='AC MULTI AXLE':
        df1 = conn.query("select bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus10 where bustype= \'AC MULTI AXLE\'")
        data = pd.DataFrame(df1)
        st.dataframe(data)
    df1=conn.query("select bustype,rating  from redbus10")


    df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    
    b=[]
    for i in df1['bustype']:
        b.append(i)


    fig = px.bar(df1, x="bustype", y="rating",color='bustype',hover_name='bustype', title="Bus Ratings")


    st.plotly_chart(fig)



#########

if var =="PRIVATE BUS TRANSPORT":

    

    conn = st.connection("postgresql", type="sql")

    

   

    with col1:
        x=st.selectbox("FROM",["HOSUR","THANJAVUR"])
    with col2:
        y=st.selectbox("TO",["CHENNAI","HOSUR"])                 
            
    if x =="HOSUR" and y =="CHENNAI":  

        df = conn.query("SELECT travels FROM redbus12;")
        a = st.selectbox("select the Private travels",df)
   
        if a=='Jabbar Travels':
            df1 = conn.query("select bustype,bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus12 where travels= \'Jabbar Travels\'")
            data = pd.DataFrame(df1)
            st.dataframe(data)
        if a=='SPS Travels':
            df1 = conn.query("select bustype,bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus12 where travels= \'SPS Travels\'")
            data = pd.DataFrame(df1)
            st.dataframe(data)
        if a=='GRS Travels':
            df1 = conn.query("select bustype,bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus12 where travels= \'GRS Travels\'")
            data = pd.DataFrame(df1)
            st.dataframe(data)

       
        df1=conn.query("select bustype,rating  from redbus12")


        df1.drop_duplicates(keep='first',subset=['bustype'],inplace=True)


    
        b=[]
        for i in df1['bustype']:
            b.append(i)


        fig = px.bar(df1, x="bustype", y="rating",color='bustype',hover_name='bustype', title="Bus Ratings")


        st.plotly_chart(fig)  

 

############
    if x=="THANJAVUR" and y=="HOSUR":        


        conn = st.connection("postgresql", type="sql")

        df = conn.query("SELECT travels FROM redbus13;")

        a = st.selectbox("select the Private travels",df)
         
          
          
   
        if a=='RKT Tours and Travels':
            df1 = conn.query("select bustype,bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus13 where travels= \'RKT Tours and Travels\'")
            data = pd.DataFrame(df1)
            st.dataframe(data)
        if a=='Rathimeena Travels B':
            df1 = conn.query("select bustype,bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus13 where travels= \'Rathimeena Travels B\'")
            data = pd.DataFrame(df1)
            st.dataframe(data)
        if a=='Dream Line Travels Pvt Ltd':
            df1 = conn.query("select bustype,bptime,dptime,bploc,dploc,rating,fare,seatleft from redbus13 where travels= \'Dream Line Travels Pvt Ltd\'")
            data = pd.DataFrame(df1)
            st.dataframe(data)

       
        df1=conn.query("select bustype,rating  from redbus13")


            
        b=[]
        for i in df1['bustype']:
            b.append(i)


        fig = px.bar(df1, x="bustype", y="rating",color='bustype',hover_name='bustype', title="Bus Ratings")


        st.plotly_chart(fig)  

    if x=="HOSUR" and y=="HOSUR":
        st.write("Sorry,i didnt scrape this route details.try the other routes")
    if x=="THANJAVUR" and y=="CHENNAI":
        st.write("Sorry,i didnt scrape this route details.try the other routes")

import time
st.html("<h6 style=\"color:red;\">click here to go to Home page</h6> ")

st.page_link("Home.py", label="Home")
st.html("<h6 style=\"color:red;\">click here to go for online Booking</h6> ")


st.link_button("RED BUS ONLINE BOOKING", 'https://www.redbus.in/')

pop=st.button("Finished")
if pop==True:
    with st.spinner(text="In progress"):
        time.sleep(5)
        st.success("Hope you have collected the required information from us.")
        
        st.balloons()
        time.sleep(3)

        st.switch_page("pages/EndPage.py")
 

    
    

