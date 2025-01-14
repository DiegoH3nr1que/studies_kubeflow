from kfp import dsl
import kfp.compiler as compiler

@dsl.component(base_image="python:3.12")
def etapa_gerar_dados():
    import subprocess
    subprocess.run(["jupyter", "nbconvert", "--execute", "--inplace", "notebook1_pre_processamento.ipynb"])

@dsl.component(base_image="python:3.12")
def etapa_treinamento():
    import subprocess
    subprocess.run(["jupyter", "nbconvert", "--execute", "--inplace", "notebook2_treinamento.ipynb"])

@dsl.pipeline(name="pipeline-teste-ml")
def pipeline_teste_ml():
    gerar_dados = etapa_gerar_dados()
    treinamento = etapa_treinamento().after(gerar_dados)

if __name__ == "__main__":
    compiler.Compiler().compile(pipeline_teste_ml, "pipeline_teste_ml.yaml")
    print("pipeline criada com sucesso!")
