from src.main.classes.models.Cuadrilla import Cuadrilla


def test_Difference():
    matrix1 = [[1,0,1],[1,0,1],[1,0,1]]
    matrix2 = [[1,0,1],[0,1,0],[0,1,1]]
    result = [[0,0,0],[1,1,1],[1,1,0]]
    cuadrilla1 = Cuadrilla(3,3,None)
    cuadrilla2 = Cuadrilla(3,3,None)
    for c in range(3):
        for r in range(3):
            cuadrilla1.setCell(c,r,matrix1[c][r])
            cuadrilla2.setCell(c,r,matrix2[c][r])
    output = cuadrilla1.checkDifference(cuadrilla2)
    assert output == result

def testLoad():
    try:
        cuadrilla = Cuadrilla(0,0,"Hard_Nivel1.txt")
    except Exception as e:
        assert False, f"Error al leer cuadrilla: {e}"
    else:
        assert True, "Exito en lectura de cuadrilla"


def test_DiscoverNums():
    cuadrilla = Cuadrilla(None,None,"Hard_Nivel1.txt")
    print()
    print(cuadrilla.__col_nums)
    assert (cuadrilla.getColumnNums() == [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]] and
            cuadrilla.getRowNums() == [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
