from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from plotly.offline import plot
import plotly.graph_objects as go


# Create your views here.
@login_required()
def home(request):
    def scatter():
        x1 = [1, 2, 3, 4]
        y1 = [30, 35, 25, 45]

        trace = go.Scatter(
            x=x1,
            y=y1
        )
        layout = dict(
            title='Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis=dict(range=[min(y1), max(y1)])
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'plot1': scatter()
    }

    return render(request, 'report/index.html', context)


@login_required()
def grafiti(request):
    return render(request, 'report/graph.html')


def datagram(request):
    return render(request, 'report/datagram.html')

def datagram2(request):
    return render(request, 'report/datagram2.html')

def dropdown(request):
    return render(request, 'report/dropdown.html')


@login_required()
def callback(request):
    return render(request, 'report/callback.html')


@login_required()
def callback2(request):
    return render(request, 'report/callback2.html')


@login_required()
def interactive(request):
    return render(request, 'report/interactive.html')


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect("/admin/")
    # Redirect to a success page.