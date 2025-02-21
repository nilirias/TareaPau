import pandas as pd
import matplotlib.pyplot as plt

def total_classes_per_student(df):
    #Cuantas clases va cada alumno
    print("Classes per student: \n", df['Alumno'].value_counts().sort_index())

def total_mfdl_class_per_student(df, modalidad):
    result = (df.groupby('Alumno')['Atributo modalidad'].value_counts().reset_index(name='count'))
    mfdl_result = result[result['Atributo modalidad'] == modalidad]
    print(mfdl_result)


def main():
    my_file = pd.read_excel("datos_AD2022.xlsx")
    my_df = pd.DataFrame(my_file)

    modalidad = input("Que modalidad quieres conocer?\n")

    result = total_mfdl_class_per_student(my_df, modalidad)

if __name__ == "__main__":
    main()