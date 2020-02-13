from enum import IntEnum

class NumbersOrder(IntEnum):
    """
    Enum que representa cada algarismo dentro do numero como um array.
    """
    TENS_THOUSANDS = 4
    UNITS_THOUSANDS = 3
    HUNDREDS = 2
    TENS = 1
    UNITS = 0


class TranslateNumber(Exception):
    """
    Classe de traducao dos numeros.
    Herda de Excecoes para disparar caso algum numero nao esteja dentro dos parametros desejados.
    """
    def __init__(self, number):
        self.numberInString =  str(number)
        self.numberSize = 0
        self.numberAsArray = []
        self.numberInFull = "zero"
        self.numberSignal = ""
        # units, tens, hundreds, teensArray
        self.unitsArray = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
        self.tensArray = ['zero', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
        self.teensArray = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                           'dezenove']
        self.hundredsArray = ['zero', 'cento', 'duzentos', 'trezentos', 'quatrocento', 'quinhentos', 'seiscentos',
                                   'setecentos', 'oitocentos', 'novecentos']

        self.validateNumber()

    def validateNumber(self):
        """
        Valida se o numero passado como parametro esta dentro dos padroes aceitos pela aplicacao.
        :return: sobe uma excecao o numero seja invalido.
        """
        try:
            self.numberInString = self.numberInString.strip()

            if self.numberInString.find('-') == 0:
                self.numberSignal = "menos "
                self.numberInString = self.numberInString.replace('-', '')

            if not self.numberInString.isdigit():
                raise TranslateNumberException("Valor invalido! Sao permitidos apenas numeros inteiros entre -99999 a 99999.")

            number = int(self.numberInString)  # converte para inteiro para retirar os zeros a esquerda.
            self.numberInString = str(number)  # volta para string para testar o tamanho maximo.

            if len(self.numberInString) > 5:
                raise TranslateNumberException("Fora da faixa permitida! Tente algum numero entre -99999 a 99999.")

        except ValueError:
            raise TranslateNumberException("")

    def __digitExtractor(self):
        """
        Transforma o numero em um array de seus algarismos.
        """
        self.numberSize = len(self.numberInString)
        self.numberAsArray = []

        for digit in reversed(range(self.numberSize)):
            self.numberAsArray.append(int(self.numberInString[digit]))

    def __solveTensThousands(self, value):
        """
        Resolve a traducao para o algarismo da dezena de milhar.
        :param value: recebe valor do algarismo correspondente.
        :return: nenhum.
        """
        if value == 1:
            if self.numberAsArray[NumbersOrder.UNITS_THOUSANDS] == 0:
                self.numberInFull += self.tensArray[value]
                self.numberInFull += " mil"
            else:
                self.numberInFull += self.teensArray[self.numberAsArray[NumbersOrder.UNITS_THOUSANDS]]
        else:
            self.numberInFull += self.tensArray[value]


    def __solveUnitsThousands(self, value, exist):
        """
        Resolve a traducao para o algarismo da unidade de milhar.
        :param value: recebe valor do algarismo correspondente.
        :param exist: recebe se existe algum algarismo anterior na hierarquia dos numeros.
        :return: retorna a existencia do respectivo algarismo.
        """
        if exist:
            if self.numberAsArray[NumbersOrder.TENS_THOUSANDS] != 1:
                self.numberInFull += " e "
                self.numberInFull += self.unitsArray[value]
            self.numberInFull += " mil"
        else:
            exist = True
            if self.numberAsArray[NumbersOrder.UNITS_THOUSANDS] != 1:
                self.numberInFull += self.unitsArray[value]
                self.numberInFull += " mil"
            else:
                self.numberInFull += "mil"
        return exist

    def __solveHundreds(self, value, exist):
        """
        Resolve a traducao para o algarismo das centenas.
        :param value: recebe valor do algarismo correspondente.
        :param exist: recebe se existe algum algarismo anterior na hierarquia dos numeros.
        :return: retorna a existencia do respectivo algarismo.
        """
        if exist:
            self.numberInFull += " "
        if value == 1:
            if self.numberAsArray[NumbersOrder.TENS] == 0 and self.numberAsArray[NumbersOrder.UNITS] == 0:
                if exist:
                    self.numberInFull += "e "
                self.numberInFull += "cem"
                self.numberSignal + self.numberInFull
            else:
                self.numberInFull += self.hundredsArray[value]
        else:
            self.numberInFull += self.hundredsArray[value]
        exist = True
        return exist


    def __solveTens(self, value, exist):
        """
        Resolve a traducao para o algarismo das dezenas.
        :param value: recebe valor do algarismo correspondente.
        :param exist: recebe se existe algum algarismo anterior na hierarquia dos numeros.
        :return: retorna a existencia do respectivo algarismo.
        """
        if exist:
            self.numberInFull += " e "
        exist = True

        if value == 1:
            if self.numberAsArray[NumbersOrder.UNITS] == 0:
                self.numberInFull += self.tensArray[value]
            else:
                self.numberInFull += self.teensArray[self.numberAsArray[NumbersOrder.UNITS]]
        else:
            self.numberInFull += self.tensArray[value]
        return exist

    def __solveUnits(self, value, exist):
        """
        Resolve a traducao para o algarismo das unidades.
        :param value: recebe valor do algarismo correspondente.
        :param exist: recebe se existe algum algarismo anterior na hierarquia dos numeros.
        :return: nenhum.
        """
        if exist:
            if self.numberAsArray[NumbersOrder.TENS] != 1:
                self.numberInFull += " e "
                self.numberInFull += self.unitsArray[value]
        else:
            self.numberInFull += self.unitsArray[value]



    def translate(self):
        """
        Faz a tradução por extenso do numero passado como parametro.
        :return: retorna o numero traduzido por extenso.
        """
        self.__digitExtractor() # Extrai cada algarismo do numero para dentro de um array (numberAsArray).

        self.numberInFull = ""
        previousExist = False

        for index in reversed(range(self.numberSize)): # Varre o array de numeros e trata cada algarismo individualmente.
            value = self.numberAsArray[index]
            if value > 0:
                if index == NumbersOrder.TENS_THOUSANDS:    # dezena de milhar
                    self.__solveTensThousands(value)
                    previousExist = True

                elif index == NumbersOrder.UNITS_THOUSANDS:    # unidade de milhar
                    previousExist = self.__solveUnitsThousands(value, previousExist)


                elif index == NumbersOrder.HUNDREDS:    # centena
                    previousExist = self.__solveHundreds(value, previousExist)


                elif index == NumbersOrder.TENS:    # dezena
                    previousExist = self.__solveTens(value, previousExist)


                elif index == NumbersOrder.UNITS:    # unidade
                    self.__solveUnits(value, previousExist)
            else:
                if index == NumbersOrder.UNITS and not previousExist:
                    self.numberInFull = "zero"
                    return self.numberInFull


        return self.numberSignal+self.numberInFull



class TranslateNumberException(Exception):
    """
    Classe que apresenta as excecoes disparadas.
    """
    def __init__(self, message):
        self.message = message