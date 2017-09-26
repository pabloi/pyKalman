import numpy as np

def updateKalman(x,P,C,D,u)

return x,P

def predictKalman(x,P,A,B,u)

return x,P

def kalmanFilter(input,output)

return xPredict,pPredict,xUpdate,pUpdate

def kalmanSmoother(input,output)

return xPredict,pPredict,xUpdate,pUpdate,xSmooth,pSmooth

def kalmanSmootherFixedLag(input,output,lag)

return

def learnQR(input,output,A,C,B,D)
#EM algorithm to estimate Q,R given dynamics

return Q,R

def learnDynamics(input,output,Nstates)
#EM algorithm to learn the full dynamical model,
#either using N generic states, or some -smoothed- history of outputs

return A,B,C,D,Q,R
