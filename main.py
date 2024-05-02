import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

# st.write("DataFrame")
st.write("Progress bar")

'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column .write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# # Slider
# condition = st.slider("How is your condition?", 0, 100, 50)
# "Your condition is ", condition, "."

# Text input
option = st.text_input("What is your hobby?")
"Your favorite hobby is", option, "."

# option = st.selectbox(
#     "What is your favorite number?",
#     list(range(1,11))
# )

#"Your favorite number is", option, "."

# # Checkbox
# if st.checkbox("Show Image"):
#     img = Image.open(r"C:\Users\yoshe\Desktop\Hiro\証明写真\IMG_E4707.JPG")
#     #img2 = Image.open("IMG_E4707.JPG")
#     st.image(img, caption="Hiro", use_column_width=True)
#     #st.image(img2, caption="Hiro", use_column_width=True)


#df = pd.DataFrame({
#    "1列目":[1,2,3,4],
#    "2列目":[10,20,30,40]
#})

#df = pd.DataFrame(
#    np.random.rand(20,3),
#    columns=["a","b", "c"]
#)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69, 139.70],
#     columns=["lat","lon"]
# )

#st.dataframe(df.style.highlight_max (axis=0))
# st.table(df.style.highlight_max (axis=0))

#st.line_chart(df)
#st.map(df)
#st.area_chart(df)
#st.bar_chart(df)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

