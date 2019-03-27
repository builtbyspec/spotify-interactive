import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Set up the chart
ratios_df = pd.read_csv('ratios.csv').dropna()
ratios_vals = ratios_df.ratio[0:5].tolist()
ratios_labels = ratios_df.Artist[0:5].tolist()
len = ratios_df.ratio.size
low_ratios_vals = ratios_df.ratio[len-5:len].tolist()
low_ratios_labels = ratios_df.Artist[len-5:len].tolist()
ratios_content = (
    'We were interested in seeing which artist’s listeners tend to stream their music more on weekends than weekdays. We focused on the most popular artists on the Top 200 chart and calculated the ratio of average streams on the weekends to the average streams on weekdays. This means that the larger numbers in this graph represent a higher difference in average number of streams on the weekends than weekdays. For example, people tended to stream Post Malone 8% more on weekends than weekdays.'
)
intro_content = (
    'As a group of ambitious statistics and computer science students first stepping foot into the world of data analysis and visualization, it would be an understatement to describe us as a group of kids in a candy shop. With a fresh understanding of statistical analysis softwares in a world where datasets are as plentiful as tweets about Donald Trump, we are excited to present our findings from our little niche of Spotify data.'
)
user_beh_content = (
    'Inspired by our own avid use of Spotify, we first wanted to delve into user behavior of Spotify, including streaming trends in response to significant events and day to day listening patterns.'
)
stream_ratio = go.Bar(
    x=ratios_vals,
    y=ratios_labels,
    text=[str(i)[0:3] + ' times more weekend streams' for i in ratios_vals],
    textposition='auto',
    orientation='h',
    marker=dict(
        color='rgba(158,202,225,0.6)',
        line=dict(
            color='rgba(8,48,107,0.7)',
            width=1
        ),
    )
)
low_stream_ratio = go.Bar(
    x=low_ratios_vals,
    y=low_ratios_labels,
    text=[str(i)[0:3] + ' times more weekday streams' for i in low_ratios_vals],
    textposition='auto',
    orientation='h',
    marker=dict(
        color='rgba(158,202,225,0.6)',
        line=dict(
            color='rgba(8,48,107,0.4)',
            width=1
        ),
    )
)

stream_ratio_data = [stream_ratio]
low_stream_ratio_data = [low_stream_ratio]
beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

########### Display the chart
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Demo",
    brand_href="#",
    sticky="top",
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Heading"),
                        html.P(
                            """\
Donec id elit non mi porta gravida at eget metus.
Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
odio dui."""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(
    children=[
        navbar,
        body,
        html.H1('Spotify'),
        html.H2('Introduction'),
        html.P(intro_content),
        html.H2('User Behavior'),
        html.P(user_beh_content),
        html.H3('Weekend to Weekday Stream Ratios'),
        html.P(ratios_content),
        dcc.Graph(
            figure={
                'data':stream_ratio_data
            }
        ),
        dcc.Graph(
            figure={
                'data':low_stream_ratio_data
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server()
