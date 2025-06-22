from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Hitung jumlah huruf di masing-masing string
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Cek apakah semua huruf di ransomNote tersedia cukup di magazine
        for char in ransom_count:
            if ransom_count[char] > magazine_count.get(char, 0):
                return False
        return True

# Contoh penggunaan:
if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct("a", "b"))       # Output: False
    print(solution.canConstruct("aa", "aab"))    # Output: True
