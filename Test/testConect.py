import unittest
from Data_Base import BancoDados
from strava.getCredential import ObterCredenciais

class TestBancoDados(unittest.TestCase):
    def TestConexaoDados(self):
        # Teste se a função BancoDados retorna uma conexão válida
        conexao = BancoDados()
        self.assertIsNotNone(conexao)
        conexao.close()  # Feche a conexão após o teste

class TestObterCredenciais(unittest.TestCase):
    def testObterCredenciais(self):
        # Teste se a função obter_credenciais retorna uma lista de credenciais não vazia
        credenciais, conexao = ObterCredenciais()
        self.assertIsNotNone(credenciais)
        self.assertIsNotNone(conexao)
        conexao.close()  # Feche a conexão após o teste

if __name__ == '__main__':
    unittest.main()
