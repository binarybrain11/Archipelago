class TextData:
    character: str
    id: int
    width: int

    def __init__(self, character: str, id: int, width: int = 6):
        self.character = character
        self.id = id
        self.width = width


all_characters: list[TextData] = [
    TextData("0", 0x00),
    TextData("1", 0x01),
    TextData("2", 0x02),
    TextData("3", 0x03),
    TextData("4", 0x04),
    TextData("5", 0x05),
    TextData("6", 0x06),
    TextData("7", 0x07),
    TextData("8", 0x08),
    TextData("9", 0x09),

    TextData("A", 0x0A),
    TextData("B", 0x0B),
    TextData("C", 0x0C),
    TextData("D", 0x0D),
    TextData("E", 0x0E),
    TextData("F", 0x0F),
    TextData("G", 0x10),
    TextData("H", 0x11),
    TextData("I", 0x12, 4),
    TextData("J", 0x13),
    TextData("K", 0x14),
    TextData("L", 0x15),
    TextData("M", 0x16),
    TextData("N", 0x17),
    TextData("O", 0x18),
    TextData("P", 0x19),
    TextData("Q", 0x1A),
    TextData("R", 0x1B),
    TextData("S", 0x1C),
    TextData("T", 0x1D),
    TextData("U", 0x1E),
    TextData("V", 0x1F),
    TextData("W", 0x20),
    TextData("X", 0x21),
    TextData("Y", 0x22),
    TextData("Z", 0x23),

    TextData("a", 0x24, 4),
    TextData("b", 0x25, 4),
    TextData("c", 0x26, 4),
    TextData("d", 0x27, 4),
    TextData("e", 0x28, 4),
    TextData("f", 0x29, 4),
    TextData("g", 0x2A, 4),
    TextData("h", 0x2B, 4),
    TextData("i", 0x2C, 2),
    TextData("j", 0x2D, 4),
    TextData("k", 0x2E, 4),
    TextData("l", 0x2F, 2),
    TextData("m", 0x30, 6),
    TextData("n", 0x31, 4),
    TextData("o", 0x32, 4),
    TextData("p", 0x33, 4),
    TextData("q", 0x34, 4),
    TextData("r", 0x35, 4),
    TextData("s", 0x36, 4),
    TextData("t", 0x37, 4),
    TextData("u", 0x38, 4),
    TextData("v", 0x39, 4),
    TextData("w", 0x3A, 6),
    TextData("x", 0x3B, 4),
    TextData("y", 0x3C, 4),
    TextData("z", 0x3D, 4),

    TextData("!", 0x3E, 4),
    TextData("?", 0x40),
    #TextData("+", 0x42),
    TextData("/", 0x44),
    TextData(":", 0x46, 4),
    TextData(".", 0x8B, 4),
    TextData("(", 0x8D, 4),
    TextData(")", 0x8E, 4),
    TextData("\"", 0x91, 4),
    TextData("'", 0x93, 4),
    TextData("♪", 0xB2, 10),
    TextData("*", 0xB5, 10),
    TextData(",", 0xD119, 4),
    TextData(".", 0xD11C, 2),

    TextData("-", 0xD11D, 2),
    TextData("+", 0xD11E, 2),
    TextData("×", 0xD11F, 2),
    TextData("÷", 0xD120, 2),

    TextData("&", 0xD9B7),
    TextData("%", 0xD9B8),

    TextData("{Aries}", 0xDA00, 10),
    TextData("{Taurus}", 0xDA01, 10),
    TextData("{Gemini}", 0xDA02, 10),
    TextData("{Cancer}", 0xDA03, 10),
    TextData("{Leo}", 0xDA04, 10),
    TextData("{Virgo}", 0xDA05, 10),
    TextData("{Libra}", 0xDA06, 10),
    TextData("{Scorpio}", 0xDA07, 10),
    TextData("{Sagittarius}", 0xDA08, 10),
    TextData("{Capricorn}", 0xDA09, 10),
    TextData("{Aquarius}", 0xDA0A, 10),
    TextData("{Pisces}", 0xDA0B, 10),
    TextData("{Serpentarius}", 0xDA0C, 10),

    TextData("=", 0xDA0C, 6),
    TextData("$", 0xDA0C, 6),
    TextData("¥", 0xDA0C, 6),

    TextData("{Newline}", 0xF8),
    TextData("{End}", 0xFE)
]

text_data_lookup = {
    text_data.character: text_data for text_data in all_characters
}