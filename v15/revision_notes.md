## Questions related to content
- p3-l72: Should we distint the detect from monitoring?
- p9-l269: I think this is correct. Can use the equation 11 on p20 to explain.
- p10-l302: Should I open a new section to talk about score clustering?
- p11-l333: I think this paragraph belongs to the `Experiments` section.
- p12-l341: I think the implementation should belongs to the section where we define `MEWMA` control charts.
- p12-l360: This inituition comes from a fact that when we do the training, score is the gradient of log-likelihood. And we update our model by the gradient with some learning rate. The learning rate is usually very small. A large deviation of score from zero may show a very small change in the parameters, and in turn show a very small change in the error rate.
- p22-l518: The logic of this section is following. We first show simulation results that score-based methods has shorter MRL1. Then, we show that how to attribute concept drift to specific covariates, when multicolinearity and nonlinearity exits. Within those examples, I also tried to present different examples, like abrupt and gradual concept drifts.
- p25-Figure6: The color is used to help describe the phenomenon. When I want to talk about specific line, I cannot use the style of line which is too hard to describe. I thought using color to pin-point specific line would be easier.
- p45-Figure21: I think the Hotelling T2 has different effects on different directions of scores, when in-control. When error is large, the score should have large norm. However, the corresponding direction of the score also has large eigenvalue. When calculating Hotelling T2, we down-weight those scores. However, when we truly have concept drift (out-of-control), no matter what data, (whether the error is large or small), we have score with large norm and those scores are much more parallel, so that we will see more seasonality in the Hotelling T2 plots, as in the prediction error plots.
- p45-Figure21: I plan to decompose the time-series first, and then do the monitoring and diagnosis analysis of concept drift on the trend and residual.
- p47-Table8: I will work on trailing yearly mean and redo the analysis.


## Other questions
- p2-l25: What kinds of papers I should cite here.
- p9-l278: We are monitoring the mean change of score. But the score we obtained is an approximated version from SGD. So I think it worths discussion, because SGD should somehow relates to the true parameters when some conditions are satistified.
- p13-Figure1: How should I show those figures?
