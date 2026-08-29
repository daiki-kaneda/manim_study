import importlib.util
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location("math_catalog", ROOT / "project/math/catalog.py")
_catalog = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules[_spec.name] = _catalog
_spec.loader.exec_module(_catalog)
VIDEOS_101_125 = _catalog.VIDEOS_101_125
VIDEOS_126_137 = _catalog.VIDEOS_126_137
VIDEOS_138_149 = _catalog.VIDEOS_138_149
VIDEOS_150_161 = _catalog.VIDEOS_150_161
VIDEOS_162_173 = _catalog.VIDEOS_162_173
VIDEOS_174_185 = _catalog.VIDEOS_174_185
VIDEOS_186_197 = _catalog.VIDEOS_186_197
VIDEOS_198_209 = _catalog.VIDEOS_198_209
VIDEOS_210_221 = _catalog.VIDEOS_210_221
VIDEOS_222_233 = _catalog.VIDEOS_222_233
VIDEOS_234_245 = _catalog.VIDEOS_234_245
VIDEOS_246_257 = _catalog.VIDEOS_246_257
VIDEOS_258_269 = _catalog.VIDEOS_258_269
VIDEOS_270_281 = _catalog.VIDEOS_270_281
VIDEOS_282_293 = _catalog.VIDEOS_282_293
VIDEOS_294_305 = _catalog.VIDEOS_294_305
VIDEOS_306_317 = _catalog.VIDEOS_306_317
VIDEOS_318_329 = _catalog.VIDEOS_318_329
VIDEOS_330_341 = _catalog.VIDEOS_330_341
VIDEOS_342_353 = _catalog.VIDEOS_342_353
VIDEOS_354_365 = _catalog.VIDEOS_354_365
VIDEOS_366_377 = _catalog.VIDEOS_366_377
VIDEOS_378_389 = _catalog.VIDEOS_378_389
VIDEOS_390_401 = _catalog.VIDEOS_390_401
VIDEOS_402_413 = _catalog.VIDEOS_402_413
VIDEOS_414_425 = _catalog.VIDEOS_414_425
VIDEOS_426_437 = _catalog.VIDEOS_426_437
VIDEOS_438_449 = _catalog.VIDEOS_438_449
VIDEOS_450_461 = _catalog.VIDEOS_450_461
VIDEOS_462_473 = _catalog.VIDEOS_462_473
VIDEOS_474_485 = _catalog.VIDEOS_474_485
VIDEOS_486_497 = _catalog.VIDEOS_486_497
VIDEOS_498_509 = _catalog.VIDEOS_498_509
VIDEOS_510_521 = _catalog.VIDEOS_510_521
VIDEOS_522_533 = _catalog.VIDEOS_522_533
VIDEOS_534_545 = _catalog.VIDEOS_534_545
VIDEOS_546_557 = _catalog.VIDEOS_546_557
VIDEOS_558_569 = _catalog.VIDEOS_558_569
VIDEOS_570_581 = _catalog.VIDEOS_570_581
VIDEOS_582_593 = _catalog.VIDEOS_582_593
VIDEOS_594_605 = _catalog.VIDEOS_594_605
VIDEOS_606_617 = _catalog.VIDEOS_606_617
VIDEOS_618_629 = _catalog.VIDEOS_618_629
VIDEOS_630_641 = _catalog.VIDEOS_630_641
VIDEOS_642_653 = _catalog.VIDEOS_642_653
VIDEOS_654_665 = _catalog.VIDEOS_654_665
VIDEOS_666_677 = _catalog.VIDEOS_666_677
VIDEOS_678_689 = _catalog.VIDEOS_678_689
VIDEOS_690_701 = _catalog.VIDEOS_690_701
VIDEOS_702_713 = _catalog.VIDEOS_702_713
VIDEOS_714_725 = _catalog.VIDEOS_714_725
VIDEOS_726_737 = _catalog.VIDEOS_726_737
VIDEOS_738_749 = _catalog.VIDEOS_738_749
VIDEOS_750_761 = _catalog.VIDEOS_750_761
VIDEOS_762_773 = _catalog.VIDEOS_762_773
VIDEOS_774_785 = _catalog.VIDEOS_774_785
VIDEOS_786_797 = _catalog.VIDEOS_786_797
VIDEOS_798_809 = _catalog.VIDEOS_798_809
VIDEOS_810_821 = _catalog.VIDEOS_810_821
VIDEOS_822_833 = _catalog.VIDEOS_822_833
VIDEOS_834_845 = _catalog.VIDEOS_834_845
VIDEOS_846_857 = _catalog.VIDEOS_846_857
VIDEOS_858_869 = _catalog.VIDEOS_858_869
VIDEOS_870_881 = _catalog.VIDEOS_870_881
VIDEOS_882_893 = _catalog.VIDEOS_882_893
VIDEOS_894_905 = _catalog.VIDEOS_894_905
VIDEOS_906_917 = _catalog.VIDEOS_906_917
VIDEOS_918_929 = _catalog.VIDEOS_918_929
VIDEOS_930_941 = _catalog.VIDEOS_930_941
VIDEOS_942_953 = _catalog.VIDEOS_942_953
VIDEOS_954_965 = _catalog.VIDEOS_954_965
VIDEOS_966_977 = _catalog.VIDEOS_966_977
VIDEOS_978_989 = _catalog.VIDEOS_978_989
VIDEOS_990_1001 = _catalog.VIDEOS_990_1001
VIDEOS_1002_1013 = _catalog.VIDEOS_1002_1013
VIDEOS_1014_1025 = _catalog.VIDEOS_1014_1025
VIDEOS_1026_1037 = _catalog.VIDEOS_1026_1037
VIDEOS_1038_1049 = _catalog.VIDEOS_1038_1049
VIDEOS_1050_1061 = _catalog.VIDEOS_1050_1061
VIDEOS_1062_1073 = _catalog.VIDEOS_1062_1073
VIDEOS_1074_1085 = _catalog.VIDEOS_1074_1085
VIDEOS_1086_1097 = _catalog.VIDEOS_1086_1097
VIDEOS_1098_1109 = _catalog.VIDEOS_1098_1109
VIDEOS_1110_1121 = _catalog.VIDEOS_1110_1121
VIDEOS_1122_1133 = _catalog.VIDEOS_1122_1133
VIDEOS_1134_1145 = _catalog.VIDEOS_1134_1145
VIDEOS_1146_1157 = _catalog.VIDEOS_1146_1157
VIDEOS_1158_1169 = _catalog.VIDEOS_1158_1169
VIDEOS_1170_1181 = _catalog.VIDEOS_1170_1181
VIDEOS_1182_1193 = _catalog.VIDEOS_1182_1193
VIDEOS_1194_1205 = _catalog.VIDEOS_1194_1205
VIDEOS_1206_1217 = _catalog.VIDEOS_1206_1217
VIDEOS_1218_1229 = _catalog.VIDEOS_1218_1229
VIDEOS_1230_1241 = _catalog.VIDEOS_1230_1241
VIDEOS_1242_1253 = _catalog.VIDEOS_1242_1253
VIDEOS_1254_1265 = _catalog.VIDEOS_1254_1265
VIDEOS_1266_1277 = _catalog.VIDEOS_1266_1277
VIDEOS_1278_1289 = _catalog.VIDEOS_1278_1289
VIDEOS_1290_1301 = _catalog.VIDEOS_1290_1301
VIDEOS_1302_1313 = _catalog.VIDEOS_1302_1313
VIDEOS_1314_1325 = _catalog.VIDEOS_1314_1325
VIDEOS_1326_1337 = _catalog.VIDEOS_1326_1337
VIDEOS_1338_1349 = _catalog.VIDEOS_1338_1349
VIDEOS_1350_1361 = _catalog.VIDEOS_1350_1361
VIDEOS_1362_1373 = _catalog.VIDEOS_1362_1373
VIDEOS_1374_1385 = _catalog.VIDEOS_1374_1385
VIDEOS_1386_1397 = _catalog.VIDEOS_1386_1397
VIDEOS_1398_1409 = _catalog.VIDEOS_1398_1409
VIDEOS_1410_1421 = _catalog.VIDEOS_1410_1421
VIDEOS_1422_1433 = _catalog.VIDEOS_1422_1433
VIDEOS_1434_1445 = _catalog.VIDEOS_1434_1445
VIDEOS_1446_1457 = _catalog.VIDEOS_1446_1457
VIDEOS_1458_1469 = _catalog.VIDEOS_1458_1469
VIDEOS_1470_1481 = _catalog.VIDEOS_1470_1481
VIDEOS_1482_1493 = _catalog.VIDEOS_1482_1493
VIDEOS_1494_1505 = _catalog.VIDEOS_1494_1505
VIDEOS_1506_1517 = _catalog.VIDEOS_1506_1517
VIDEOS_1518_1529 = _catalog.VIDEOS_1518_1529
VIDEOS_1530_1541 = _catalog.VIDEOS_1530_1541
VIDEOS_1542_1553 = _catalog.VIDEOS_1542_1553
VIDEOS_1554_1565 = _catalog.VIDEOS_1554_1565
VIDEOS_1566_1577 = _catalog.VIDEOS_1566_1577
VIDEOS_1578_1589 = _catalog.VIDEOS_1578_1589
VIDEOS_1590_1601 = _catalog.VIDEOS_1590_1601
VIDEOS_1602_1613 = _catalog.VIDEOS_1602_1613
VIDEOS_1614_1625 = _catalog.VIDEOS_1614_1625
VIDEOS_1626_1637 = _catalog.VIDEOS_1626_1637
VIDEOS_1638_1649 = _catalog.VIDEOS_1638_1649
VIDEOS_1650_1661 = _catalog.VIDEOS_1650_1661
VIDEOS_1662_1673 = _catalog.VIDEOS_1662_1673
VIDEOS_1674_1685 = _catalog.VIDEOS_1674_1685
VIDEOS_1686_1697 = _catalog.VIDEOS_1686_1697
VIDEOS_1698_1709 = _catalog.VIDEOS_1698_1709
VIDEOS_1710_1721 = _catalog.VIDEOS_1710_1721
VIDEOS_1722_1733 = _catalog.VIDEOS_1722_1733
VIDEOS_1734_1745 = _catalog.VIDEOS_1734_1745
VIDEOS_1746_1757 = _catalog.VIDEOS_1746_1757
VIDEOS_1758_1769 = _catalog.VIDEOS_1758_1769
VIDEOS_1770_1781 = _catalog.VIDEOS_1770_1781
VIDEOS_1782_1793 = _catalog.VIDEOS_1782_1793


class CatalogTests(unittest.TestCase):
    def test_numbers_are_101_to_125(self):
        nums = [v.number for v in VIDEOS_101_125]
        self.assertEqual(nums, list(range(101, 126)))

    def test_numbers_are_126_to_137(self):
        nums = [v.number for v in VIDEOS_126_137]
        self.assertEqual(nums, list(range(126, 138)))

    def test_numbers_are_138_to_149(self):
        nums = [v.number for v in VIDEOS_138_149]
        self.assertEqual(nums, list(range(138, 150)))

    def test_numbers_are_150_to_161(self):
        nums = [v.number for v in VIDEOS_150_161]
        self.assertEqual(nums, list(range(150, 162)))

    def test_numbers_are_162_to_173(self):
        nums = [v.number for v in VIDEOS_162_173]
        self.assertEqual(nums, list(range(162, 174)))

    def test_numbers_are_174_to_185(self):
        nums = [v.number for v in VIDEOS_174_185]
        self.assertEqual(nums, list(range(174, 186)))

    def test_numbers_are_186_to_197(self):
        nums = [v.number for v in VIDEOS_186_197]
        self.assertEqual(nums, list(range(186, 198)))

    def test_numbers_are_198_to_209(self):
        nums = [v.number for v in VIDEOS_198_209]
        self.assertEqual(nums, list(range(198, 210)))

    def test_numbers_are_210_to_221(self):
        nums = [v.number for v in VIDEOS_210_221]
        self.assertEqual(nums, list(range(210, 222)))

    def test_numbers_are_222_to_233(self):
        nums = [v.number for v in VIDEOS_222_233]
        self.assertEqual(nums, list(range(222, 234)))

    def test_numbers_are_234_to_245(self):
        nums = [v.number for v in VIDEOS_234_245]
        self.assertEqual(nums, list(range(234, 246)))

    def test_numbers_are_246_to_257(self):
        nums = [v.number for v in VIDEOS_246_257]
        self.assertEqual(nums, list(range(246, 258)))

    def test_numbers_are_258_to_269(self):
        nums = [v.number for v in VIDEOS_258_269]
        self.assertEqual(nums, list(range(258, 270)))

    def test_numbers_are_270_to_281(self):
        nums = [v.number for v in VIDEOS_270_281]
        self.assertEqual(nums, list(range(270, 282)))

    def test_numbers_are_282_to_293(self):
        nums = [v.number for v in VIDEOS_282_293]
        self.assertEqual(nums, list(range(282, 294)))

    def test_numbers_are_294_to_305(self):
        nums = [v.number for v in VIDEOS_294_305]
        self.assertEqual(nums, list(range(294, 306)))

    def test_numbers_are_306_to_317(self):
        nums = [v.number for v in VIDEOS_306_317]
        self.assertEqual(nums, list(range(306, 318)))

    def test_numbers_are_318_to_329(self):
        nums = [v.number for v in VIDEOS_318_329]
        self.assertEqual(nums, list(range(318, 330)))

    def test_numbers_are_330_to_341(self):
        nums = [v.number for v in VIDEOS_330_341]
        self.assertEqual(nums, list(range(330, 342)))

    def test_numbers_are_342_to_353(self):
        nums = [v.number for v in VIDEOS_342_353]
        self.assertEqual(nums, list(range(342, 354)))

    def test_numbers_are_354_to_365(self):
        nums = [v.number for v in VIDEOS_354_365]
        self.assertEqual(nums, list(range(354, 366)))

    def test_numbers_are_366_to_377(self):
        nums = [v.number for v in VIDEOS_366_377]
        self.assertEqual(nums, list(range(366, 378)))

    def test_numbers_are_378_to_389(self):
        nums = [v.number for v in VIDEOS_378_389]
        self.assertEqual(nums, list(range(378, 390)))

    def test_numbers_are_390_to_401(self):
        nums = [v.number for v in VIDEOS_390_401]
        self.assertEqual(nums, list(range(390, 402)))

    def test_numbers_are_402_to_413(self):
        nums = [v.number for v in VIDEOS_402_413]
        self.assertEqual(nums, list(range(402, 414)))

    def test_numbers_are_414_to_425(self):
        nums = [v.number for v in VIDEOS_414_425]
        self.assertEqual(nums, list(range(414, 426)))

    def test_numbers_are_426_to_437(self):
        nums = [v.number for v in VIDEOS_426_437]
        self.assertEqual(nums, list(range(426, 438)))

    def test_numbers_are_438_to_449(self):
        nums = [v.number for v in VIDEOS_438_449]
        self.assertEqual(nums, list(range(438, 450)))

    def test_numbers_are_450_to_461(self):
        nums = [v.number for v in VIDEOS_450_461]
        self.assertEqual(nums, list(range(450, 462)))

    def test_numbers_are_462_to_473(self):
        nums = [v.number for v in VIDEOS_462_473]
        self.assertEqual(nums, list(range(462, 474)))

    def test_numbers_are_474_to_485(self):
        nums = [v.number for v in VIDEOS_474_485]
        self.assertEqual(nums, list(range(474, 486)))

    def test_numbers_are_486_to_497(self):
        nums = [v.number for v in VIDEOS_486_497]
        self.assertEqual(nums, list(range(486, 498)))

    def test_numbers_are_498_to_509(self):
        nums = [v.number for v in VIDEOS_498_509]
        self.assertEqual(nums, list(range(498, 510)))

    def test_numbers_are_510_to_521(self):
        nums = [v.number for v in VIDEOS_510_521]
        self.assertEqual(nums, list(range(510, 522)))

    def test_numbers_are_522_to_533(self):
        nums = [v.number for v in VIDEOS_522_533]
        self.assertEqual(nums, list(range(522, 534)))

    def test_numbers_are_534_to_545(self):
        nums = [v.number for v in VIDEOS_534_545]
        self.assertEqual(nums, list(range(534, 546)))

    def test_numbers_are_546_to_557(self):
        nums = [v.number for v in VIDEOS_546_557]
        self.assertEqual(nums, list(range(546, 558)))

    def test_numbers_are_558_to_569(self):
        nums = [v.number for v in VIDEOS_558_569]
        self.assertEqual(nums, list(range(558, 570)))

    def test_numbers_are_570_to_581(self):
        nums = [v.number for v in VIDEOS_570_581]
        self.assertEqual(nums, list(range(570, 582)))

    def test_numbers_are_582_to_593(self):
        nums = [v.number for v in VIDEOS_582_593]
        self.assertEqual(nums, list(range(582, 594)))

    def test_numbers_are_594_to_605(self):
        nums = [v.number for v in VIDEOS_594_605]
        self.assertEqual(nums, list(range(594, 606)))

    def test_numbers_are_606_to_617(self):
        nums = [v.number for v in VIDEOS_606_617]
        self.assertEqual(nums, list(range(606, 618)))

    def test_numbers_are_618_to_629(self):
        nums = [v.number for v in VIDEOS_618_629]
        self.assertEqual(nums, list(range(618, 630)))

    def test_numbers_are_630_to_641(self):
        nums = [v.number for v in VIDEOS_630_641]
        self.assertEqual(nums, list(range(630, 642)))

    def test_numbers_are_642_to_653(self):
        nums = [v.number for v in VIDEOS_642_653]
        self.assertEqual(nums, list(range(642, 654)))

    def test_numbers_are_654_to_665(self):
        nums = [v.number for v in VIDEOS_654_665]
        self.assertEqual(nums, list(range(654, 666)))

    def test_numbers_are_666_to_677(self):
        nums = [v.number for v in VIDEOS_666_677]
        self.assertEqual(nums, list(range(666, 678)))

    def test_numbers_are_678_to_689(self):
        nums = [v.number for v in VIDEOS_678_689]
        self.assertEqual(nums, list(range(678, 690)))

    def test_numbers_are_690_to_701(self):
        nums = [v.number for v in VIDEOS_690_701]
        self.assertEqual(nums, list(range(690, 702)))

    def test_numbers_are_702_to_713(self):
        nums = [v.number for v in VIDEOS_702_713]
        self.assertEqual(nums, list(range(702, 714)))

    def test_numbers_are_714_to_725(self):
        nums = [v.number for v in VIDEOS_714_725]
        self.assertEqual(nums, list(range(714, 726)))

    def test_numbers_are_726_to_737(self):
        nums = [v.number for v in VIDEOS_726_737]
        self.assertEqual(nums, list(range(726, 738)))

    def test_numbers_are_738_to_749(self):
        nums = [v.number for v in VIDEOS_738_749]
        self.assertEqual(nums, list(range(738, 750)))

    def test_numbers_are_750_to_761(self):
        nums = [v.number for v in VIDEOS_750_761]
        self.assertEqual(nums, list(range(750, 762)))

    def test_numbers_are_762_to_773(self):
        nums = [v.number for v in VIDEOS_762_773]
        self.assertEqual(nums, list(range(762, 774)))

    def test_numbers_are_774_to_785(self):
        nums = [v.number for v in VIDEOS_774_785]
        self.assertEqual(nums, list(range(774, 786)))

    def test_numbers_are_786_to_797(self):
        nums = [v.number for v in VIDEOS_786_797]
        self.assertEqual(nums, list(range(786, 798)))

    def test_numbers_are_798_to_809(self):
        nums = [v.number for v in VIDEOS_798_809]
        self.assertEqual(nums, list(range(798, 810)))

    def test_numbers_are_810_to_821(self):
        nums = [v.number for v in VIDEOS_810_821]
        self.assertEqual(nums, list(range(810, 822)))

    def test_numbers_are_822_to_833(self):
        nums = [v.number for v in VIDEOS_822_833]
        self.assertEqual(nums, list(range(822, 834)))

    def test_numbers_are_834_to_845(self):
        nums = [v.number for v in VIDEOS_834_845]
        self.assertEqual(nums, list(range(834, 846)))

    def test_numbers_are_846_to_857(self):
        nums = [v.number for v in VIDEOS_846_857]
        self.assertEqual(nums, list(range(846, 858)))

    def test_numbers_are_858_to_869(self):
        nums = [v.number for v in VIDEOS_858_869]
        self.assertEqual(nums, list(range(858, 870)))

    def test_numbers_are_870_to_881(self):
        nums = [v.number for v in VIDEOS_870_881]
        self.assertEqual(nums, list(range(870, 882)))


    def test_numbers_are_882_to_893(self):
        nums = [v.number for v in VIDEOS_882_893]
        self.assertEqual(nums, list(range(882, 894)))


    def test_numbers_are_894_to_905(self):
        nums = [v.number for v in VIDEOS_894_905]
        self.assertEqual(nums, list(range(894, 906)))


    def test_numbers_are_906_to_917(self):
        nums = [v.number for v in VIDEOS_906_917]
        self.assertEqual(nums, list(range(906, 918)))


    def test_numbers_are_918_to_929(self):
        nums = [v.number for v in VIDEOS_918_929]
        self.assertEqual(nums, list(range(918, 930)))


    def test_numbers_are_930_to_941(self):
        nums = [v.number for v in VIDEOS_930_941]
        self.assertEqual(nums, list(range(930, 942)))


    def test_numbers_are_942_to_953(self):
        nums = [v.number for v in VIDEOS_942_953]
        self.assertEqual(nums, list(range(942, 954)))


    def test_numbers_are_954_to_965(self):
        nums = [v.number for v in VIDEOS_954_965]
        self.assertEqual(nums, list(range(954, 966)))


    def test_numbers_are_966_to_977(self):
        nums = [v.number for v in VIDEOS_966_977]
        self.assertEqual(nums, list(range(966, 978)))


    def test_numbers_are_978_to_989(self):
        nums = [v.number for v in VIDEOS_978_989]
        self.assertEqual(nums, list(range(978, 990)))


    def test_numbers_are_990_to_1001(self):
        nums = [v.number for v in VIDEOS_990_1001]
        self.assertEqual(nums, list(range(990, 1002)))


    def test_numbers_are_1002_to_1013(self):
        nums = [v.number for v in VIDEOS_1002_1013]
        self.assertEqual(nums, list(range(1002, 1014)))


    def test_numbers_are_1014_to_1025(self):
        nums = [v.number for v in VIDEOS_1014_1025]
        self.assertEqual(nums, list(range(1014, 1026)))


    def test_numbers_are_1026_to_1037(self):
        nums = [v.number for v in VIDEOS_1026_1037]
        self.assertEqual(nums, list(range(1026, 1038)))


    def test_numbers_are_1038_to_1049(self):
        nums = [v.number for v in VIDEOS_1038_1049]
        self.assertEqual(nums, list(range(1038, 1050)))


    def test_numbers_are_1050_to_1061(self):
        nums = [v.number for v in VIDEOS_1050_1061]
        self.assertEqual(nums, list(range(1050, 1062)))


    def test_numbers_are_1062_to_1073(self):
        nums = [v.number for v in VIDEOS_1062_1073]
        self.assertEqual(nums, list(range(1062, 1074)))


    def test_numbers_are_1074_to_1085(self):
        nums = [v.number for v in VIDEOS_1074_1085]
        self.assertEqual(nums, list(range(1074, 1086)))


    def test_numbers_are_1086_to_1097(self):
        nums = [v.number for v in VIDEOS_1086_1097]
        self.assertEqual(nums, list(range(1086, 1098)))


    def test_numbers_are_1098_to_1109(self):
        nums = [v.number for v in VIDEOS_1098_1109]
        self.assertEqual(nums, list(range(1098, 1110)))


    def test_numbers_are_1110_to_1121(self):
        nums = [v.number for v in VIDEOS_1110_1121]
        self.assertEqual(nums, list(range(1110, 1122)))


    def test_numbers_are_1122_to_1133(self):
        nums = [v.number for v in VIDEOS_1122_1133]
        self.assertEqual(nums, list(range(1122, 1134)))


    def test_numbers_are_1134_to_1145(self):
        nums = [v.number for v in VIDEOS_1134_1145]
        self.assertEqual(nums, list(range(1134, 1146)))


    def test_numbers_are_1146_to_1157(self):
        nums = [v.number for v in VIDEOS_1146_1157]
        self.assertEqual(nums, list(range(1146, 1158)))


    def test_numbers_are_1158_to_1169(self):
        nums = [v.number for v in VIDEOS_1158_1169]
        self.assertEqual(nums, list(range(1158, 1170)))


    def test_numbers_are_1170_to_1181(self):
        nums = [v.number for v in VIDEOS_1170_1181]
        self.assertEqual(nums, list(range(1170, 1182)))


    def test_numbers_are_1182_to_1193(self):
        nums = [v.number for v in VIDEOS_1182_1193]
        self.assertEqual(nums, list(range(1182, 1194)))


    def test_numbers_are_1194_to_1205(self):
        nums = [v.number for v in VIDEOS_1194_1205]
        self.assertEqual(nums, list(range(1194, 1206)))


    def test_numbers_are_1206_to_1217(self):
        nums = [v.number for v in VIDEOS_1206_1217]
        self.assertEqual(nums, list(range(1206, 1218)))


    def test_numbers_are_1218_to_1229(self):
        nums = [v.number for v in VIDEOS_1218_1229]
        self.assertEqual(nums, list(range(1218, 1230)))


    def test_numbers_are_1230_to_1241(self):
        nums = [v.number for v in VIDEOS_1230_1241]
        self.assertEqual(nums, list(range(1230, 1242)))


    def test_numbers_are_1242_to_1253(self):
        nums = [v.number for v in VIDEOS_1242_1253]
        self.assertEqual(nums, list(range(1242, 1254)))


    def test_numbers_are_1254_to_1265(self):
        nums = [v.number for v in VIDEOS_1254_1265]
        self.assertEqual(nums, list(range(1254, 1266)))


    def test_numbers_are_1266_to_1277(self):
        nums = [v.number for v in VIDEOS_1266_1277]
        self.assertEqual(nums, list(range(1266, 1278)))


    def test_numbers_are_1278_to_1289(self):
        nums = [v.number for v in VIDEOS_1278_1289]
        self.assertEqual(nums, list(range(1278, 1290)))


    def test_numbers_are_1290_to_1301(self):
        nums = [v.number for v in VIDEOS_1290_1301]
        self.assertEqual(nums, list(range(1290, 1302)))


    def test_numbers_are_1302_to_1313(self):
        nums = [v.number for v in VIDEOS_1302_1313]
        self.assertEqual(nums, list(range(1302, 1314)))


    def test_numbers_are_1314_to_1325(self):
        nums = [v.number for v in VIDEOS_1314_1325]
        self.assertEqual(nums, list(range(1314, 1326)))


    def test_numbers_are_1326_to_1337(self):
        nums = [v.number for v in VIDEOS_1326_1337]
        self.assertEqual(nums, list(range(1326, 1338)))


    def test_numbers_are_1338_to_1349(self):
        nums = [v.number for v in VIDEOS_1338_1349]
        self.assertEqual(nums, list(range(1338, 1350)))


    def test_numbers_are_1350_to_1361(self):
        nums = [v.number for v in VIDEOS_1350_1361]
        self.assertEqual(nums, list(range(1350, 1362)))


    def test_numbers_are_1362_to_1373(self):
        nums = [v.number for v in VIDEOS_1362_1373]
        self.assertEqual(nums, list(range(1362, 1374)))


    def test_numbers_are_1374_to_1385(self):
        nums = [v.number for v in VIDEOS_1374_1385]
        self.assertEqual(nums, list(range(1374, 1386)))


    def test_numbers_are_1386_to_1397(self):
        nums = [v.number for v in VIDEOS_1386_1397]
        self.assertEqual(nums, list(range(1386, 1398)))


    def test_numbers_are_1398_to_1409(self):
        nums = [v.number for v in VIDEOS_1398_1409]
        self.assertEqual(nums, list(range(1398, 1410)))


    def test_numbers_are_1410_to_1421(self):
        nums = [v.number for v in VIDEOS_1410_1421]
        self.assertEqual(nums, list(range(1410, 1422)))


    def test_numbers_are_1422_to_1433(self):
        nums = [v.number for v in VIDEOS_1422_1433]
        self.assertEqual(nums, list(range(1422, 1434)))


    def test_numbers_are_1434_to_1445(self):
        nums = [v.number for v in VIDEOS_1434_1445]
        self.assertEqual(nums, list(range(1434, 1446)))


    def test_numbers_are_1446_to_1457(self):
        nums = [v.number for v in VIDEOS_1446_1457]
        self.assertEqual(nums, list(range(1446, 1458)))


    def test_numbers_are_1458_to_1469(self):
        nums = [v.number for v in VIDEOS_1458_1469]
        self.assertEqual(nums, list(range(1458, 1470)))


    def test_numbers_are_1470_to_1481(self):
        nums = [v.number for v in VIDEOS_1470_1481]
        self.assertEqual(nums, list(range(1470, 1482)))


    def test_numbers_are_1482_to_1493(self):
        nums = [v.number for v in VIDEOS_1482_1493]
        self.assertEqual(nums, list(range(1482, 1494)))


    def test_numbers_are_1494_to_1505(self):
        nums = [v.number for v in VIDEOS_1494_1505]
        self.assertEqual(nums, list(range(1494, 1506)))


    def test_numbers_are_1506_to_1517(self):
        nums = [v.number for v in VIDEOS_1506_1517]
        self.assertEqual(nums, list(range(1506, 1518)))


    def test_numbers_are_1518_to_1529(self):
        nums = [v.number for v in VIDEOS_1518_1529]
        self.assertEqual(nums, list(range(1518, 1530)))


    def test_numbers_are_1530_to_1541(self):
        nums = [v.number for v in VIDEOS_1530_1541]
        self.assertEqual(nums, list(range(1530, 1542)))


    def test_numbers_are_1542_to_1553(self):
        nums = [v.number for v in VIDEOS_1542_1553]
        self.assertEqual(nums, list(range(1542, 1554)))


    def test_numbers_are_1554_to_1565(self):
        nums = [v.number for v in VIDEOS_1554_1565]
        self.assertEqual(nums, list(range(1554, 1566)))


    def test_numbers_are_1566_to_1577(self):
        nums = [v.number for v in VIDEOS_1566_1577]
        self.assertEqual(nums, list(range(1566, 1578)))


    def test_numbers_are_1578_to_1589(self):
        nums = [v.number for v in VIDEOS_1578_1589]
        self.assertEqual(nums, list(range(1578, 1590)))


    def test_numbers_are_1590_to_1601(self):
        nums = [v.number for v in VIDEOS_1590_1601]
        self.assertEqual(nums, list(range(1590, 1602)))


    def test_numbers_are_1602_to_1613(self):
        nums = [v.number for v in VIDEOS_1602_1613]
        self.assertEqual(nums, list(range(1602, 1614)))


    def test_numbers_are_1614_to_1625(self):
        nums = [v.number for v in VIDEOS_1614_1625]
        self.assertEqual(nums, list(range(1614, 1626)))


    def test_numbers_are_1626_to_1637(self):
        nums = [v.number for v in VIDEOS_1626_1637]
        self.assertEqual(nums, list(range(1626, 1638)))


    def test_numbers_are_1638_to_1649(self):
        nums = [v.number for v in VIDEOS_1638_1649]
        self.assertEqual(nums, list(range(1638, 1650)))


    def test_numbers_are_1650_to_1661(self):
        nums = [v.number for v in VIDEOS_1650_1661]
        self.assertEqual(nums, list(range(1650, 1662)))


    def test_numbers_are_1662_to_1673(self):
        nums = [v.number for v in VIDEOS_1662_1673]
        self.assertEqual(nums, list(range(1662, 1674)))


    def test_numbers_are_1674_to_1685(self):
        nums = [v.number for v in VIDEOS_1674_1685]
        self.assertEqual(nums, list(range(1674, 1686)))


    def test_numbers_are_1686_to_1697(self):
        nums = [v.number for v in VIDEOS_1686_1697]
        self.assertEqual(nums, list(range(1686, 1698)))


    def test_numbers_are_1698_to_1709(self):
        nums = [v.number for v in VIDEOS_1698_1709]
        self.assertEqual(nums, list(range(1698, 1710)))


    def test_numbers_are_1710_to_1721(self):
        nums = [v.number for v in VIDEOS_1710_1721]
        self.assertEqual(nums, list(range(1710, 1722)))


    def test_numbers_are_1722_to_1733(self):
        nums = [v.number for v in VIDEOS_1722_1733]
        self.assertEqual(nums, list(range(1722, 1734)))


    def test_numbers_are_1734_to_1745(self):
        nums = [v.number for v in VIDEOS_1734_1745]
        self.assertEqual(nums, list(range(1734, 1746)))


    def test_numbers_are_1746_to_1757(self):
        nums = [v.number for v in VIDEOS_1746_1757]
        self.assertEqual(nums, list(range(1746, 1758)))


    def test_numbers_are_1758_to_1769(self):
        nums = [v.number for v in VIDEOS_1758_1769]
        self.assertEqual(nums, list(range(1758, 1770)))


    def test_numbers_are_1770_to_1781(self):
        nums = [v.number for v in VIDEOS_1770_1781]
        self.assertEqual(nums, list(range(1770, 1782)))


    def test_numbers_are_1782_to_1793(self):
        nums = [v.number for v in VIDEOS_1782_1793]
        self.assertEqual(nums, list(range(1782, 1794)))

    def test_each_scene_file_defines_the_class(self):
        for video in (
            *VIDEOS_101_125,
            *VIDEOS_126_137,
            *VIDEOS_138_149,
            *VIDEOS_150_161,
            *VIDEOS_162_173,
            *VIDEOS_174_185,
            *VIDEOS_186_197,
            *VIDEOS_198_209,
            *VIDEOS_210_221,
            *VIDEOS_222_233,
            *VIDEOS_234_245,
            *VIDEOS_246_257,
            *VIDEOS_258_269,
            *VIDEOS_270_281,
            *VIDEOS_282_293,
            *VIDEOS_294_305,
            *VIDEOS_306_317,
            *VIDEOS_318_329,
            *VIDEOS_330_341,
            *VIDEOS_342_353,
            *VIDEOS_354_365,
            *VIDEOS_366_377,
            *VIDEOS_378_389,
            *VIDEOS_390_401,
            *VIDEOS_402_413,
            *VIDEOS_414_425,
            *VIDEOS_426_437,
            *VIDEOS_438_449,
            *VIDEOS_450_461,
            *VIDEOS_462_473,
            *VIDEOS_474_485,
            *VIDEOS_486_497,
            *VIDEOS_498_509,
            *VIDEOS_510_521,
            *VIDEOS_522_533,
            *VIDEOS_534_545,
            *VIDEOS_546_557,
            *VIDEOS_558_569,
            *VIDEOS_570_581,
            *VIDEOS_582_593,
            *VIDEOS_594_605,
            *VIDEOS_606_617,
            *VIDEOS_618_629,
            *VIDEOS_630_641,
            *VIDEOS_642_653,
            *VIDEOS_654_665,
            *VIDEOS_666_677,
            *VIDEOS_678_689,
            *VIDEOS_690_701,
            *VIDEOS_702_713,
            *VIDEOS_714_725,
            *VIDEOS_726_737,
            *VIDEOS_738_749,
            *VIDEOS_750_761,
            *VIDEOS_762_773,
            *VIDEOS_774_785,
            *VIDEOS_786_797,
            *VIDEOS_798_809,
            *VIDEOS_810_821,
            *VIDEOS_822_833,
            *VIDEOS_834_845,
            *VIDEOS_846_857,
            *VIDEOS_858_869,
            *VIDEOS_870_881,
            *VIDEOS_882_893,
            *VIDEOS_894_905,
            *VIDEOS_906_917,
            *VIDEOS_918_929,
            *VIDEOS_930_941,
            *VIDEOS_942_953,
            *VIDEOS_954_965,
            *VIDEOS_966_977,
            *VIDEOS_978_989,
            *VIDEOS_990_1001,
            *VIDEOS_1002_1013,
            *VIDEOS_1014_1025,
            *VIDEOS_1026_1037,
            *VIDEOS_1038_1049,
            *VIDEOS_1050_1061,
            *VIDEOS_1062_1073,
            *VIDEOS_1074_1085,
            *VIDEOS_1086_1097,
            *VIDEOS_1098_1109,
            *VIDEOS_1110_1121,
            *VIDEOS_1122_1133,
            *VIDEOS_1134_1145,
            *VIDEOS_1146_1157,
            *VIDEOS_1158_1169,
            *VIDEOS_1170_1181,
            *VIDEOS_1182_1193,
            *VIDEOS_1194_1205,
            *VIDEOS_1206_1217,
            *VIDEOS_1218_1229,
            *VIDEOS_1230_1241,
            *VIDEOS_1242_1253,
            *VIDEOS_1254_1265,
            *VIDEOS_1266_1277,
            *VIDEOS_1278_1289,
            *VIDEOS_1290_1301,
            *VIDEOS_1302_1313,
            *VIDEOS_1314_1325,
            *VIDEOS_1326_1337,
            *VIDEOS_1338_1349,
            *VIDEOS_1350_1361,
            *VIDEOS_1362_1373,
            *VIDEOS_1374_1385,
            *VIDEOS_1386_1397,
            *VIDEOS_1398_1409,
            *VIDEOS_1410_1421,
            *VIDEOS_1422_1433,
            *VIDEOS_1434_1445,
            *VIDEOS_1446_1457,
            *VIDEOS_1458_1469,
            *VIDEOS_1470_1481,
            *VIDEOS_1482_1493,
            *VIDEOS_1494_1505,
            *VIDEOS_1506_1517,
            *VIDEOS_1518_1529,
            *VIDEOS_1530_1541,
            *VIDEOS_1542_1553,
            *VIDEOS_1554_1565,
            *VIDEOS_1566_1577,
            *VIDEOS_1578_1589,
            *VIDEOS_1590_1601,
            *VIDEOS_1602_1613,
            *VIDEOS_1614_1625,
            *VIDEOS_1626_1637,
            *VIDEOS_1638_1649,
            *VIDEOS_1650_1661,
            *VIDEOS_1662_1673,
            *VIDEOS_1674_1685,
            *VIDEOS_1686_1697,
            *VIDEOS_1698_1709,
            *VIDEOS_1710_1721,
            *VIDEOS_1722_1733,
            *VIDEOS_1734_1745,
            *VIDEOS_1746_1757,
            *VIDEOS_1758_1769,
            *VIDEOS_1770_1781,
            *VIDEOS_1782_1793,
        ):
            path = ROOT / video.path
            self.assertTrue(path.is_file(), msg=video.path)
            text = path.read_text(encoding="utf-8")
            self.assertIn(f"class {video.scene}(", text)
            self.assertTrue("JapaneseScene" in text or "PacedScene" in text, msg=video.path)
            story = path.parent / "storyboard.md"
            self.assertTrue(story.is_file(), msg=str(story))


if __name__ == "__main__":
    unittest.main()
