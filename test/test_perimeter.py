import numpy as np
import unittest

from .context import stltovoxel  # noqa: F401
from stltovoxel import perimeter


class TestPerimeter(unittest.TestCase):
    def test_lines_to_pixels(self):
        test = [[(0, 0, 0), (3, 0, 0)],
                [(9, 9, 0), (3, 9, 0)],
                [(3, 0, 0), (9, 9, 0)],
                [(3, 9, 0), (0, 0, 0)]]
        actual = np.zeros((13, 13), dtype=bool)
        perimeter.lines_to_voxels(test, actual)
        expected = [
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(expected, actual.astype(int).tolist())

    def test_cross_line(self):
        pixels = np.zeros((100, 100), dtype=bool)
        # when z=133, x=55 at Eiffel_tower_sample.STL, resolution=100
        lines = [
            ((55.183775000510195, 42.91771076583979, 133.0), (54.664478438939994, 42.91190079807315, 133.0)),
            ((55.05365382117602, 48.399582783540694, 133.0), (54.28259953472679, 48.399582783540694, 133.0)),
            ((54.72938801464095, 51.1054056827822, 133.0), (55.21085292933077, 51.10540695761318, 133.0)),
            ((55.17312327125145, 54.131620716008165, 133.0), (54.72938801464095, 54.13161531213461, 133.0)),
            ((54.28259953472679, 48.399582783540694, 133.0), (55.05365382117602, 48.399582783540694, 133.0)),
            ((55.05365382117602, 50.600419560857354, 133.0), (54.28259953472679, 50.600419560857354, 133.0)),
            ((54.72938801464095, 44.868384133402195, 133.0), (55.21085292933077, 44.868386286857266, 133.0)),
            ((55.183775000510195, 56.0822892341602, 133.0), (54.664478438939994, 56.088101893431286, 133.0)),
            ((55.17312327125145, 47.89459328407937, 133.0), (54.72938801464095, 47.894596812904574, 133.0))
        ]
        x = 55
        # have assert or Exception in paint_y_axis()
        perimeter.paint_y_axis(lines, pixels, x)

        pixels = np.zeros((512, 512), dtype=bool)
        # python stltovoxel.py data/Model.stl data/Model.png 512
        lines = [
            ((164.09973516910665, 210.30269491875893, 292.0), (162.88562081679706, 211.99251111205203, 292.0)),
            ((163.6486419675717, 400.48144695905705, 292.0), (162.98334736067383, 399.69497154303264, 292.0)),
            ((163.12053950901193, 399.083573336035, 292.0), (162.75365385590837, 399.3013424292643, 292.0)),
            ((162.09875517681738, 155.11154635650513, 292.0), (163.03976252838729, 154.67417098395714, 292.0)),
            ((162.922318771988, 177.86366465114196, 292.0), (164.23901942305332, 178.47337917148627, 292.0))
        ]
        x = 163
        # have assert or Exception in paint_y_axis()
        perimeter.paint_y_axis(lines, pixels, x)

        pixels = np.zeros((1024, 1024), dtype=bool)
        # python stltovoxel.py data/Model.stl data/Model.png 1024
        lines = [
            ((478.1953748963024, 685.5971369469289, 390.0), (474.987648897627, 682.7858002239518, 390.0)),
            ((478.6458712360894, 708.867925235024, 390.0), (476.80635493021373, 709.6422457310404, 390.0)),
            ((476.8066506675348, 704.1490977931986, 390.0), (478.9686356730549, 707.4220913093288, 390.0)),
            ((475.51186735002426, 568.0120562125561, 390.0), (477.6508098598742, 568.5847941911843, 390.0)),
            ((476.9319294711261, 643.620807438934, 390.0), (477.55874656005545, 643.8324324309802, 390.0)),
            ((477.6538957136681, 644.1949502652121, 390.0), (476.50764488546764, 647.3730220867313, 390.0)),
            ((477.1678215835232, 574.2494597833005, 390.0), (475.625871469434, 575.2964648366983, 390.0)),
            ((476.71719857029177, 276.879543451238, 390.0), (478.92572111642284, 275.85023482493455, 390.0)),
            ((475.7395840585432, 726.9413018914573, 390.0), (477.6455166631113, 728.1006656939942, 390.0)),
            ((480.1531171455746, 424.8577588241842, 390.0), (474.50256297902456, 421.5806451519458, 390.0)),
            ((476.33245691945507, 647.8338656180929, 390.0), (477.3585664525454, 650.5878998039989, 390.0))
        ]
        x = 477
        # have assert or Exception in paint_y_axis()
        perimeter.paint_y_axis(lines, pixels, x)


if __name__ == '__main__':
    unittest.main()
