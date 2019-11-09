% Read in agreement counts 
agreement_rates = readtable('Agreement Counts.xlsx');

% table to an array
agreement_rates = table2array(agreement_rates);

% set upper and lower bounds a choose an x0 (multistart is going to be
% used, so this choice really doesn't matter)
lb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
ub = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1];
x0 = lb;

% find a solution for c1; multistart a couple thousand times to avoid local
% minima
rng default % For reproducibility
options = optimoptions(@fmincon,'Algorithm','sqp','MaxFunctionEvaluations',100000,'MaxIterations',10000);
problem = createOptimProblem('fmincon','objective',...
    @(x)c1(x),'x0',x0,'lb',lb,'ub',ub,'options',options,'nonlcon',@(x)Unsupervised_Error_Constraints(x,agreement_rates));
ms = MultiStart;
ms = MultiStart(ms,'UseParallel',true);
[opt_c1,opt_cost_c1] = run(ms,problem,3000)

% define second cost function (much simpler)
c2 = @(x) x(1) + x(2) + x(3) + x(4) + x(5);

% find a solution for c1; multistart a couple thousand times to avoid local
% minima
rng default % For reproducibility
options = optimoptions(@fmincon,'Algorithm','sqp','MaxFunctionEvaluations',100000,'MaxIterations',10000);
problem = createOptimProblem('fmincon','objective',...
    @(x)c2(x),'x0',x0,'lb',lb,'ub',ub,'options',options,'nonlcon',@(x)Unsupervised_Error_Constraints(x,agreement_rates));
ms = MultiStart;
ms = MultiStart(ms,'UseParallel',true);
[opt_c2,opt_cost_c2] = run(ms,problem,3000)