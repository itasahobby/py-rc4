from unittest import main, TestCase
from rc4 import Rc4

valid_key = bytearray.fromhex("deadbeef")
valid_data = bytearray.fromhex("5468697320697320612073616d706c652074657874")


class TestRc4(TestCase):
    def test_encrypt(self):
        # Testing encryption
        rc4 = Rc4(key=valid_key)
        encrypted = rc4.encrypt(valid_data)
        self.assertNotEqual(encrypted, rc4.encrypt(valid_data))
        rc4 = Rc4(key=valid_key)
        self.assertEqual(encrypted, rc4.encrypt(valid_data))
        # Testing data types
        self.assertTrue(isinstance(encrypted, bytearray))

    def test_decrypt(self):
        rc4 = Rc4(key=valid_key)
        encrypted = rc4.encrypt(valid_data)
        rc4 = Rc4(key=valid_key)
        self.assertEqual(valid_data, rc4.decrypt(encrypted))


if __name__ == '__main__':
    main()
