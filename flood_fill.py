from typing import List
from typing import Optional

image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr1 = 1
sc1 = 1
color1 = 2


# class Solution:
#     def floodFill(
#         self, image: List[List[int]], sr: int, sc: int, color: int
#     ) -> List[List[int]]:
#         if image[sr][sc] == color or image == None:
#             return image
#         initial = image[sr][sc]
#         self.fill(image, sr, sc, initial, color)
#         return image

#     def fill(self, image, r, c, initial, color):
#         if (
#             r < 0
#             or r > len(image) - 1
#             or c < 0
#             or c > len(image[0]) - 1
#             or image[r][c] != initial
#         ):
#             return

#         image[r][c] = color
#         self.fill(image, r + 1, c, initial, color)
#         self.fill(image, r - 1, c, initial, color)
#         self.fill(image, r, c + 1, initial, color)
#         self.fill(image, r, c - 1, initial, color)


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image == None or image[sr][sc] == color:
            return image

        starting_pixel = image[sr][sc]
        self.fill(image, sr, sc, starting_pixel, color)
        return image

    def fill(self, image, r, c, starting_pixel, color):
        if (
            r < 0
            or r > len(image) - 1
            or c < 0
            or c > len(image[0]) - 1
            or image[r][c] != starting_pixel
        ):
            return

        image[r][c] = color
        self.fill(image, r + 1, c, starting_pixel, color)
        self.fill(image, r - 1, c, starting_pixel, color)
        self.fill(image, r, c + 1, starting_pixel, color)
        self.fill(image, r, c - 1, starting_pixel, color)


sol = Solution().floodFill(image1, sr1, sc1, color1)
print(sol)
