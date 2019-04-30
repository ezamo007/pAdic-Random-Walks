import delta_calc as dc
import rw_visualize as vis
import rw_probs as prob

#To plot random walks with after 'steps' number of steps, execute the command below.

#Example
#vis.plot_rw(steps = 10, num_walks = 2)



#To save a random walk animation, execute the command below. Tail is the tail length, the number of points trailing the current one.
#vis.gen_rw_animation(steps = 200, num_walks = 50, tail = 20, window = [x_min, x_max, y_min, y_max])

#Example
#vis.gen_rw_animation(100,30,10)


#To visualize the random walk probabilities of the first step,
#call plot_rw_prob from prob with a color 3-tuple of your favorite color.

#Example
prob.plot_rw_prob((0.0,0.5,1.0))
