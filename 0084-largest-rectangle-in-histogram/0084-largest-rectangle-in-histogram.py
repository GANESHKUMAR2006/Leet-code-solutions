class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        area=0
        heights.append(0)
        for right in range(len(heights)):
            while st and heights[right]<heights[st[-1]]:
                top=st.pop()
                height=heights[top]
                if not st:
                    width=right
                else:
                    width=right-st[-1]-1
                area=max(area,height*width)
            st.append(right)
        return area