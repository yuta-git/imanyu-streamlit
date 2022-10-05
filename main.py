import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Display the progress bar')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('Show texts in the right column')
if button:
  right_column.write('Here is the right column')

expander = st.expander('Contact')
expander.write('Write the content of contact')

# text = st.text_input('Tell me your hobby.')
# condition = st.slider('How is your condition?', 0, 10, 5)

# 'Your hobby:', text
# 'Condition:', condition

# text = st.sidebar.text_input('Tell me your hobby.')
# condition = st.sidebar.slider('How is your condition?', 0, 10, 5)

# option = st.selectbox(
#   'Tell me your favorite number',
#   list(range(1, 11))
# )
# 'Your favorite number is ', option, '.'

# if st.checkbox('Show Image'):
#   img = Image.open('sample.jpg')
#   st.image(img, caption='Jogo', use_column_width=True)

# st.write('DataFrame')
# df = pd.DataFrame(
#   # '1列目': [1, 2, 3, 4],
#   # '2列目': [10, 20, 30, 40]
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#   columns = ['lat', 'lon']
# )
# st.map(df)


# st.table(df.style.highlight_max(axis=0))
