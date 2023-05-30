import json
from shapely.geometry import shape, mapping
from shapely.ops import unary_union

# Ruta de los archivos GeoJSON
ruta_poligono_mayor = 'sao_paulo_general.geojson'
ruta_areas_mas_pequenas = 'spo_microzones.geojson'
ruta_salida = 'ruta_del_archivo_salida.geojson'


# Crear los objetos de geometría de Shapely para el polígono mayor y las áreas más pequeñas
poligono_mayor = shape(data_poligono_mayor['features'][0]['geometry'])
areas_mas_pequenas = [shape(feature['geometry']) for feature in data_areas_mas_pequenas['features']]

# Restar las áreas más pequeñas del polígono mayor
resultado = poligono_mayor.difference(unary_union(areas_mas_pequenas))

# Crear un nuevo GeoJSON con el resultado combinado
resultado_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": mapping(resultado),
            "properties": {}
        }
    ]
}

# Escribir el resultado en un archivo GeoJSON
with open(ruta_salida, 'w') as file:
    json.dump(resultado_geojson, file)