from matplotlib import pyplot as plt
from collections import Counter

'''
 Example #1: Simple line chart - GDP over time
'''
def make_chart_simple_line_chart():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    # Create a line chart, years on x-axis, gdp on y-axis
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    # Add a title
    plt.title("Nominal GDP")

    # Add a label to the y-axis
    plt.ylabel("Billions of $ (USD)")
    plt.show()

'''
 Example #2: Simple bar chart - academy awards per movie
'''
def make_chart_simple_bar_chart():
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    # bars are by default width 0.8, so we'll add 0.1 to the left coordinates
    # so that each bar is centered
    xs = [i + 0.1 for i, _ in enumerate(movies)]

    # plot bars with left x-coordinates [xs], heights [num_oscars]
    plt.bar(xs, num_oscars)
    plt.ylabel("# of Academy Awards")
    plt.title("My Favorite Movies")

    # label x-axis with movie names at bar centers
    plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

    plt.show()

'''
 Example #3: Using Counter to show a histogram
'''
def make_chart_histogram():
    grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)

    plt.bar([x for x in histogram.keys()], # shift each bar to the left by 4
            list(histogram.values()),                # give each bar its correct height
            8)                                 # give each bar a width of 8
    plt.axis([-5, 105, 0, 5])                  # x-axis from -5 to 105,
                                               # y-axis from 0 to 5
    plt.xticks([10 * i for i in range(11)])    # x-axis labels at 0, 10, ..., 100
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution of Exam 1 Grades")
    plt.show()

'''
 Example #4: Misleading axis can create confusing graphs
'''
def make_chart_misleading_y_axis(mislead=True):
    # TODO

'''
 Example #5: Adding multiple series to a line chart
'''
def make_chart_several_line_charts():
    # TODO

'''
 Example #6: Scatterplots for showing relationships between related data
'''
def make_chart_scatterplot_axes(equal_axes=False):
    # TODO

'''
 Main Routine
'''
if __name__ == "__main__":

    # make_chart_simple_line_chart()
    #
    # make_chart_simple_bar_chart()
    #
    # make_chart_histogram()
    #
    # make_chart_misleading_y_axis(mislead=True)
    #
    # make_chart_misleading_y_axis(mislead=False)
    #
    # make_chart_several_line_charts()
    #
    # make_chart_scatterplot_axes(equal_axes=False)
    #
    # make_chart_scatterplot_axes(equal_axes=True)
    #
    # make_chart_pie_chart()