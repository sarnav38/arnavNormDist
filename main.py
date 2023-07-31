import streamlit as st
import plotly.figure_factory as ff
import numpy as np
from numpy.random import normal

st.title('Statistics Visualize Tool')
st.title('Interactive Normal Distribution Curve')

with st.sidebar:
    option = st.selectbox(':blue[Navigation]', ('Normal Distribution', 'KDE'))
    mean_loc = st.slider('Mean', -10.0, 10.0, 1.0, 0.1)
    std_loc = st.slider('Standard Deviation', 0.0, 5.0, 2.0, 0.1)
    PDF_Curve = st.checkbox('PDF_Curve')
    Histogram = st.checkbox('Histogram')
    b_s = number = st.number_input('Bin Size', 0.0, 10.0, 0.5, 0.1)

with st.container():
    np.random.seed(42)
    data = normal(loc=0, scale=1, size=1000)
    data1 = normal(loc=mean_loc, scale=std_loc, size=1000)
    # Group data together
    hist_data = [data, data1]
    group_labels = ['Original', 'Changes']
    # Create distplot with custom bin_size
    if PDF_Curve and Histogram:
        fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.5, b_s],
                                 show_rug=False)
    elif PDF_Curve and not Histogram:
        fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.5, b_s],
                                 show_rug=False, show_hist=False)
    elif Histogram and not PDF_Curve:
        fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.5, b_s],
                                 show_rug=False, show_curve=False)
    else:
        st.warning('Click either PDF_Curve or Histogram', icon="⚠️")
        fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.5, b_s],
                                 show_rug=False, show_curve=False, show_hist=False)

    fig.update_layout(autosize=True, width=900, height=700)
    st.plotly_chart(fig, theme=None)

col1, col2 = st.columns(2, gap='large')

with col1:
    st.subheader('Descriptive Statistics for Original Data')
    st.markdown(f'Mean: :red[{data.mean()}]')
    st.markdown(f'Std: :red[{data.std()}]')
    st.markdown(f'Max: :red[{data.max()}]')
    st.markdown(f'Min: :red[{data.min()}]')
    st.markdown(f'Min: :red[0.5]')

with col2:
    st.subheader('Descriptive Statistics for Changed Data')
    st.markdown(f'Mean: :red[{data1.mean()}]')
    st.markdown(f'Std: :red[{data1.std()}]')
    st.markdown(f'Max: :red[{data1.max()}]')
    st.markdown(f'Min: :red[{data1.min()}]')
    st.markdown(f'Min: :red[{b_s}]')
