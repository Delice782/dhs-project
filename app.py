import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Rwanda DHS 2025 Health Gains", layout="centered")

st.title("Rwanda's Maternal and Child Health Progress, 2020 to 2025")
st.write("Source: Rwanda Demographic and Health Survey 2025, National Institute of Statistics of Rwanda")

survey_years = [2020, 2025]

total_fertility_rate_values = [4.1, 3.7]
maternal_mortality_ratio_values = [203, 149]
under_five_mortality_values = [45, 36]
stunting_prevalence_values = [33, 27]
antenatal_care_four_visits_values = [47, 78]

indicator_names = [
    "Total Fertility Rate (children per woman)",
    "Maternal Mortality Ratio (deaths per 100,000 live births)",
    "Under Five Mortality (deaths per 1,000 live births)",
    "Stunting Prevalence (percent of children under five)",
    "Antenatal Care, Four or More Visits (percent of women)",
]

indicator_values_lookup = {
    indicator_names[0]: total_fertility_rate_values,
    indicator_names[1]: maternal_mortality_ratio_values,
    indicator_names[2]: under_five_mortality_values,
    indicator_names[3]: stunting_prevalence_values,
    indicator_names[4]: antenatal_care_four_visits_values,
}

selected_indicator = st.selectbox("Choose an indicator to view", indicator_names)

selected_values = indicator_values_lookup[selected_indicator]

value_2020 = selected_values[0]
value_2025 = selected_values[1]

if value_2020 != 0:
    percent_change = ((value_2025 - value_2020) / value_2020) * 100
else:
    percent_change = 0

trend_figure = go.Figure()
trend_figure.add_trace(
    go.Scatter(
        x=survey_years,
        y=selected_values,
        mode="lines+markers+text",
        text=selected_values,
        textposition="top center",
        line=dict(width=4),
        marker=dict(size=12),
    )
)
trend_figure.update_layout(
    title=selected_indicator,
    xaxis_title="Survey Year",
    yaxis_title="Value",
    xaxis=dict(tickmode="array", tickvals=survey_years),
)

st.plotly_chart(trend_figure, use_container_width=True)

if percent_change < 0:
    st.success(f"{selected_indicator} fell by {abs(percent_change):.1f} percent between 2020 and 2025.")
elif percent_change > 0:
    st.info(f"{selected_indicator} rose by {abs(percent_change):.1f} percent between 2020 and 2025.")
else:
    st.write(f"{selected_indicator} did not change between 2020 and 2025.")

st.divider()
st.subheader("Total Fertility Rate by Province, 2025")

province_names = ["Kigali", "National Average", "East Province"]
province_fertility_values = [3.1, 3.7, 4.0]

province_figure = go.Figure()
province_figure.add_trace(
    go.Bar(
        x=province_names,
        y=province_fertility_values,
        text=province_fertility_values,
        textposition="outside",
    )
)
province_figure.update_layout(
    title="Total Fertility Rate by Province, 2025",
    yaxis_title="Children per Woman",
)

st.plotly_chart(province_figure, use_container_width=True)

st.divider()
st.subheader("Summary of All Five Indicators")

summary_rows = []
for indicator_name in indicator_names:
    indicator_values = indicator_values_lookup[indicator_name]
    starting_value = indicator_values[0]
    ending_value = indicator_values[1]
    summary_rows.append(
        {
            "Indicator": indicator_name,
            "2020 Value": starting_value,
            "2025 Value": ending_value,
        }
    )

st.table(summary_rows)