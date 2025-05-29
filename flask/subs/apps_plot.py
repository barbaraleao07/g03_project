from flask import render_template, session 
from classes.patient import Patient
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64

def apps_plot():
    engine = create_engine('sqlite:///' + filename + 'Patient.db')

    df_patient = pd.read_sql('Patient', con=engine)

    # ------------------ Gráfico 1: Pacientes por Condição Médica ------------------
    result = df_patient['condition'].value_counts()
    conditions = result.index.tolist()
    counts = result.values

    fig1, ax1 = plt.subplots()
    ax1.bar(conditions, counts, color='skyblue')
    ax1.set_xlabel('Condição Médica')
    ax1.set_ylabel('Número de Pacientes')
    ax1.set_title('Pacientes por Condição Médica')
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

    buf1 = io.BytesIO()
    plt.tight_layout()
    fig1.savefig(buf1, format='png')
    plt.close(fig1)
    buf1.seek(0)
    image1 = base64.b64encode(buf1.getvalue()).decode('utf-8')

    # ------------------ Gráfico 2: Pacientes por Faixa Etária ------------------
    bins = [0, 18, 35, 50, 65, 80, 100]
    labels = ['0-17', '18-34', '35-49', '50-64', '65-79', '80+']
    df_patient['age_group'] = pd.cut(df_patient['age'], bins=bins, labels=labels)

    age_group_counts = df_patient['age_group'].value_counts().sort_index()

    fig2, ax2 = plt.subplots()
    ax2.bar(age_group_counts.index.astype(str), age_group_counts.values, color='mediumseagreen')
    ax2.set_xlabel('Faixa Etária')
    ax2.set_ylabel('Número de Pacientes')
    ax2.set_title('Pacientes por Faixa Etária')
    plt.setp(ax2.get_xticklabels(), rotation=0)

    buf2 = io.BytesIO()
    plt.tight_layout()
    fig2.savefig(buf2, format='png')
    plt.close(fig2)
    buf2.seek(0)
    image2 = base64.b64encode(buf2.getvalue()).decode('utf-8')

    return render_template("plot.html", image=image1, image2=image2, ulogin=session.get("user"))
