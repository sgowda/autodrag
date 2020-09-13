def draw_box(fig, p0, size):
    rect = patches.Rectangle(p0, size[0] * fig.dpi, size[1] * fig.dpi, linewidth=1, edgecolor='r', facecolor='none')
    fig.patches.extend([rect])

def fig_bounding_box_rescale_factor_to_canvas(fig, margin=0.02):
    """Rescale plots to take up the entire canvas without changing their aspect ratio

    margin: in inches
    """
    axes = fig.get_axes()
    axes_bounds = [get_axis_bounds(fig, ax, scaled=True) for ax in axes]
    print('axes bounds', np.vstack(axes_bounds))

    box_relative = _extended_bounding_box(axes_bounds)
    fig_size = fig.get_size_inches() - np.array([margin, margin])
    canvas_size = np.hstack([fig_size, fig_size])
    box_in = box_relative * canvas_size

    box_size_in = box_in[2:] - box_in[:2]
    scale_factor = np.min(fig_size / box_size_in) #* 0.9 # TODO eliminate fudge factor

    for ax in axes:
        bounds = get_plot_bounds(fig, ax) * canvas_size * scale_factor
        new_size_rel = (bounds[2:] - bounds[:2]) / fig_size
        x0y0 = bounds[:2] / fig_size

        ax.set_position(np.hstack([x0y0, new_size_rel]))

    return scale_factor


def fit_to_canvas(fig):
    for k in range(3):
        reposition(fig)
        canvas_rescale_factor = fig_bounding_box_rescale_factor_to_canvas(fig)
        plt.draw()
