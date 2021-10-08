import unittest
import numpy as np

from pymcdm import methods
from pymcdm.methods.mcda_method import MCDA_method


class TestMCDA(unittest.TestCase):

    def test_validation(self):
        with self.assertRaises(ValueError):
            body = MCDA_method()
            matrix = np.array([[1, 2, 3], [1, 2, 3]])
            weights = np.array([0.5, 0.5])
            types = np.array([1, -1, -1])
            body._validate_input_data(matrix, weights, types)


class TestARAS(unittest.TestCase):
    """ Test output method with reference:
    [1] Stanujkic, D., Djordjevic, B., & Karabasevic, D. (2015). Selection of
    candidates in the process of recruitment and selection of personnel based on the SWARA and ARAS methods.
    Quaestus, (7), 53.
    """

    def test_output(self):
        body = methods.ARAS()
        matrix = np.array([[4.64, 3.00, 3.00, 3.00, 2.88, 3.63],
                           [4.00, 4.00, 4.64, 3.56, 3.63, 5.00],
                           [3.30, 4.31, 3.30, 4.00, 3.30, 4.00],
                           [2.62, 5.00, 4.22, 4.31, 5.00, 5.00]])

        weights = np.array([0.28, 0.25, 0.19, 0.15, 0.08, 0.04])
        types = np.array([1, 1, 1, 1, 1, 1])

        output = [0.74, 0.86, 0.78, 0.86]
        output_method = [round(preference, 2) for preference in body(matrix, weights, types)]

        self.assertListEqual(output, output_method)


class TestCOCOSO(unittest.TestCase):
    """ Test output method with reference:
    [1] Yazdani, M., Zarate, P., Zavadskas, E. K., & Turskis, Z. (2019). A
    Combined Compromise Solution (CoCoSo) method for multi-criteria decision-making problems. Management Decision.
    """

    def test_output(self):
        body = methods.COCOSO()
        matrix = np.array([[60, 0.4, 2540, 500, 990],
                           [6.35, 0.15, 1016, 3000, 1041],
                           [6.8, 0.1, 1727.2, 1500, 1676],
                           [10, 0.2, 1000, 2000, 965],
                           [2.5, 0.1, 560, 500, 915],
                           [4.5, 0.08, 1016, 350, 508],
                           [3, 0.1, 1778, 1000, 920]])
        weights = np.array([0.036, 0.192, 0.326, 0.326, 0.12])
        types = np.array([1, -1, 1, 1, 1])

        output = [2.041, 2.788, 2.882, 2.416, 1.299, 1.443, 2.519]
        output_method = [round(preference, 3) for preference in body(matrix, weights, types)]

        self.assertListEqual(output, output_method)


class TestCODAS(unittest.TestCase):
    """ Test output method with reference:
    [1] Badi, I., Shetwan, A. G., & Abdulshahed, A. M. (2017, September).
    Supplier selection using COmbinative Distance-based ASsessment (CODAS) method for multi-criteria decision-making.
    In Proceedings of The 1st International Conference on Management, Engineering and Environment (ICMNEE) (pp.
    395-407).
    """

    def test_output(self):
        body = methods.CODAS()
        matrix = np.array([[45, 3600, 45, 0.9],
                           [25, 3800, 60, 0.8],
                           [23, 3100, 35, 0.9],
                           [14, 3400, 50, 0.7],
                           [15, 3300, 40, 0.8],
                           [28, 3000, 30, 0.6]])
        types = np.array([1, -1, 1, 1])
        weights = np.array([0.2857, 0.3036, 0.2321, 0.1786])

        output = [1.3914, 0.3411, -0.2170, -0.5381, -0.7292, -0.2481]
        output_method = [round(preference, 4) for preference in body(matrix, weights, types)]

        self.assertListEqual(output, output_method)


class TestCOMET(unittest.TestCase):
    """ Test output method with reference:
    [1] Paradowski, B., Bączkiewicz, A., & Watrąbski, J. (2021). Towards
    proper consumer choices-MCDM based product selection. Procedia Computer Science, 192, 1347-1358.
    """

    def test_output(self):
        matrix = np.array([[64, 128, 2.9, 4.3, 3.2, 280, 495, 24763, 3990],
                           [28, 56, 3.1, 3.8, 3.8, 255, 417, 12975, 2999],
                           [8, 16, 3.5, 5.3, 4.8, 125, 636, 5725, 539],
                           [12, 24, 3.7, 4.8, 4.5, 105, 637, 8468, 549],
                           [10, 20, 3.7, 5.3, 4.9, 125, 539, 6399, 499],
                           [8, 16, 3.6, 4.4, 4.0, 65, 501, 4834, 329],
                           [6, 12, 3.7, 4.6, 4.2, 65, 604, 4562, 299],
                           [16, 32, 3.4, 4.9, 4.2, 105, 647, 10428, 799],
                           [8, 16, 3.6, 5.0, 4.5, 125, 609, 5615, 399],
                           [18, 36, 3.0, 4.8, 4.3, 165, 480, 8848, 979],
                           [24, 48, 3.8, 4.5, 4.0, 280, 509, 13552, 1399],
                           [28, 56, 2.5, 3.8, 2.8, 205, 376, 8585, 10000]])

        cvalues = np.vstack((
            np.min(matrix, axis=0),
            np.max(matrix, axis=0)
        )).T
        types = np.array([1, 1, 1, 1, 1, -1, 1, 1, -1])
        weights = np.array([1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9])

        body = methods.COMET(cvalues, methods.COMET.topsis_rate_function(weights, types))

        output = [0.5433, 0.3447, 0.6115, 0.6168, 0.6060, 0.4842, 0.5516, 0.6100, 0.5719, 0.4711, 0.4979, 0.1452]
        output_method = [round(preference, 4) for preference in body(matrix)]

        self.assertListEqual(output, output_method)
