% Notation: This fitness function is for demonstration 
function [cost, Info] = jFitnessFunction(feat,label,X,HO)
if sum(X == 1) == 0
  cost = inf;
else
  Info = jwrapperKNN(feat(:, X == 1),label,HO);
  cost=Info(3);

end
end
function error = jwrapperKNN(sFeat,label,HO)
%---// Parameter setting for k-value of KNN //
k = 5; 
xtrain = sFeat(HO.training == 1,:);
ytrain = label(HO.training == 1); 
xvalid = sFeat(HO.test == 1,:); 
yvalid = label(HO.test == 1); 
Model     = fitcknn(xtrain,ytrain,'NumNeighbors',k); 
pred      = predict(Model,xvalid);
bb = confusionmatStats(yvalid,pred);

acc=mean(bb.accuracy);
fscore=mean(bb.Fscore);
loss= 1-acc;
error = [ acc fscore loss];

end
