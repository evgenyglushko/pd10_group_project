class BasicWord:

    def __init__(self, word: str, subwords: list):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f"'{self.word}'.BasicWord"

    def check_subword_in_subwords(self, subword: str) -> bool:
        """
        Проверяет наличие подслова в списке подслов
        :param subword:
        :return: bool
        """
        return subword in self.subwords

    def get_subwords_quantity(self) -> int:
        """
        Возвращает количество подслов
        :return: int
        """
        return len(self.subwords)
