# Pydantic e validação de dados
## Método POST
É utilizado para enviar dados para o servidor. Esses dados geralmente enviados em formato JSON ou XML.
É o método HTTP mais comum para enviar dados, como formulários de contato, informações de registero ou outros
dados que precisam ser processados pelo servidor.
O método POST envia os dados no corpo da requisição HTTP, ao invés da URL.
## Método POST no FastAPI
No FastAPI utilizamos o @app.post para definir uma rota.
## Request Body
É a parte de uma requisição HTTP que contém os dados que você deseja enviar ao servidor.
Dados em formatos JSON, XML.
## Pydantic
É uma biblioteca Python que fornece validação de dados e tratamento de erros.
Define modelos de dados usando anotações de tipo Python.
fornece validação automática de dados, o que significa que ele verifica se os dados fornecidos correspondem ao modelo de 
dados definido.
## Modelos de Dados
São estruturas que definem a forma e o tipo. 

```
from fastapi import FastAPI

app  = FastAPI()



@app.get("/products/{product_id}")
def read_root(product_id: int):
    for product in products:
        if product_id == product["id"]:
            return {
                product
            }
    return {
        "message": "Product not found"
    }
    
@app.get("/products")
def get_products(min_price: float = None):
    
    if min_price:
        filter_products = [product for product in products if product["price"] >= min_price]
    return {
        filter_products
    }
    ```
## Validator
Para casos em que seja necessário adicionar validações personalizadas, é possível usar o validator.
é uma funcionalidade do pydantic usada para adicionar validações personalizadas em campos de um modelo de dados.
ele permite criar regras de validação adicionais além das tipagens definidas nos campos.

```
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, field_validator

class Student(BaseModel):
    name: str
    email: EmailStr
    age: int
    
app  = FastAPI()

@app.post("/student")
def create_student(student: Student):
    return {
        "aluno": student
    }
    ```

