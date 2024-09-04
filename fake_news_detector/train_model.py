import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Carga de datos
fake_news = pd.read_csv('fake.csv')
true_news = pd.read_csv('true.csv')

# Añadir una columna "label" para indicar si la noticia es falsa o verdadera
fake_news['label'] = 0  # 0 para noticias falsas
true_news['label'] = 1  # 1 para noticias verdaderas

# Combinar los datasets en uno solo
df = pd.concat([fake_news, true_news], axis=0)

# Seleccionar las columnas relevantes
X = df['text']
y = df['label']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creación del pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Entrenamiento del modelo
model.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(model, 'fake_news_model.pkl')
