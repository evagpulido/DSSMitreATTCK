import csv
from owlready2 import *

# Carga tu ontología en Protege
onto = get_ontology("../Ontologia/OntologiaDSS.owl").load()

# Ruta del archivo CSV
archivo_csv = "../RegistrosTrafico/logsPrueba.csv"

# Diccionario para realizar un seguimiento de los números asignados a cada tipo de ataque
numeros_ataques = {}

# Lee el archivo CSV y crea las instancias correspondientes
with open(archivo_csv, "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        label = row["Label"]
        ataque_class = getattr(onto, label, None)
        
        if ataque_class is not None and issubclass(ataque_class, onto.Ataque):
            # Verifica si el tipo de ataque ya tiene un número asignado
            if label in numeros_ataques:
                numero = numeros_ataques[label] + 1
                numeros_ataques[label] = numero
            else:
                numero = 1
                numeros_ataques[label] = numero
            
            # Crea el nombre de la instancia con el formato TipoDeAtaque-Número
            nombre_instancia = "{}-{}".format(label, numero)
            
            # Crea una instancia de la subclase de Ataque con el nombre correspondiente
            ataque_instance = ataque_class(nombre_instancia)

            # Agrega la instancia a la clase general "Ataque"
            ataque_instance.is_a.append(onto.Ataque)
            
            # Agrega una data property "tipoDeAtaque" con el valor del Label
            ataque_instance.tipoDeAtaque.append(label)

            # Agrega la data property "flowId" con el valor de la columna "Flow ID"
            ataque_instance.flowId.append(row["Flow ID"])
            
            # Agrega la data property "timestamp" con el valor de la columna "Timestamp"
            ataque_instance.timestamp.append(row["Timestamp"])
            
    

# Relaciones entre los ataques y las tácticas
for ataque in onto.Ataque.instances():
    tipo_ataque = ataque.tipoDeAtaque[0]  # Suponiendo que solo hay un valor para tipoDeAtaque
    
    if tipo_ataque == "Bot":
        # Relaciona el ataque con la táctica
        tactica = onto.search_one(nombreTactica="Comando_y_control")
        ataque.usaTactica.append(tactica)
        # Obtene la técnica basada en el nombre de sub-tecnica ("ya tenemos creadas las instancias de subtecnicas en el esqueleto")
        subTecnica = onto.search_one(nombreSubTecnica="Proxy")
        # Relaciona el ataque con la sub-técnica
        ataque.usaSubTecnica.append(subTecnica)
    elif tipo_ataque == "DDoS":
        tactica = onto.search_one(nombreTactica="Impacto")
        ataque.usaTactica.append(tactica)
        subTecnica = onto.search_one(nombreSubTecnica="Denegacion_de_servicio_de_red")
        ataque.usaSubTecnica.append(subTecnica)
    elif tipo_ataque == "FTP-Patator":
        tactica = onto.search_one(nombreTactica="Acceso_a_credenciales")
        ataque.usaTactica.append(tactica)
        subTecnica = onto.search_one(nombreSubTecnica="Fuerza_bruta")
        ataque.usaSubTecnica.append(subTecnica)
    elif tipo_ataque == "Infiltration":
        tactica1 = onto.search_one(nombreTactica="Acceso_a_credenciales")
        ataque.usaTactica.append(tactica1)
        tactica2 = onto.search_one(nombreTactica="Acceso_inicial")
        ataque.usaTactica.append(tactica2)
        tactica3 = onto.search_one(nombreTactica="Reconocimiento")
        ataque.usaTactica.append(tactica3)
        tactica4 = onto.search_one(nombreTactica="Comando_y_control")
        ataque.usaTactica.append(tactica4)
        subTecnicas = ["Phishing", "Acceso_remoto", "Fuerza_bruta", "Recopilar_info_victima"]
        for subTecnica_nombre in subTecnicas:
            subTecnica = onto.search_one(nombreSubTecnica=subTecnica_nombre)
            ataque.usaSubTecnica.append(subTecnica)
    elif tipo_ataque == "PortScan":
        tactica1 = onto.search_one(nombreTactica="Reconocimiento")
        ataque.usaTactica.append(tactica1)
        tactica2 = onto.search_one(nombreTactica="Discovery")
        ataque.usaTactica.append(tactica2)
        subTecnicas = ["Active_scanning", "Network_service_discovery"]
        for subTecnica_nombre in subTecnicas:
            subTecnica = onto.search_one(nombreSubTecnica=subTecnica_nombre)
            ataque.usaSubTecnica.append(subTecnica)
    elif tipo_ataque == "SSH-Patator":
        tactica = onto.search_one(nombreTactica="Acceso_a_credenciales")
        ataque.usaTactica.append(tactica)
        subTecnica = onto.search_one(nombreSubTecnica="Fuerza_bruta")
        ataque.usaSubTecnica.append(subTecnica)
    elif tipo_ataque == "WebAttack_BruteForce":
        tactica = onto.search_one(nombreTactica="Acceso_a_credenciales")
        ataque.usaTactica.append(tactica)
        subTecnica = onto.search_one(nombreSubTecnica="Fuerza_bruta")
        ataque.usaSubTecnica.append(subTecnica)
    elif tipo_ataque == "WebAttack_SqlInjection":
        tactica = onto.search_one(nombreTactica="Impacto")
        ataque.usaTactica.append(tactica)
        subTecnica = onto.search_one(nombreSubTecnica="Manipulacion_datos")
        ataque.usaSubTecnica.append(subTecnica)
    elif tipo_ataque == "WebAttack_XSS":
        tactica = onto.search_one(nombreTactica="Acceso_inicial")
        ataque.usaTactica.append(tactica)
        subTecnica = onto.search_one(nombreSubTecnica="Command_scripting_interpreter")
        ataque.usaSubTecnica.append(subTecnica)
    else:
        print("No se encontró una relación adecuada para el tipo de ataque:", tipo_ataque)



    

for ataque in onto.Ataque.instances():
    # Obtener todas las técnicas asociadas al ataque
    tecnicas = ataque.usaSubTecnica
    # print("El ataque", ataque, "usa las técnicas:", tecnicas)

    # Relaciona el ataque con los individuos de mitigación de cada técnica
    for tecnica in tecnicas:
        mitigaciones = tecnica.seMitigaCon
        # print("La tecnica", tecnica, "se mitiga con:", mitigaciones)

        for mitigacion in mitigaciones:
            ataque.ataqueSeMitigaCon.append(mitigacion)

 

# Guarda la instancia en la ontología
sync_reasoner()
onto.save("../Ontologia/OntologiaDSS_Completa.owl")
