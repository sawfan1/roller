# this is a helper file for handling vectors
import math

def aminusb(a,b):
  return (a[0] -b[0], a[1]-b[1])

def dot(A, B):
  return A[0] * B[0] + A[1]*B[1]

def length(V):
  return math.sqrt(V[0]**2+V[1]**2)

def normalize(V):
  l=length(V)

  if l==0:
    return (0, 0)

  return (V[0]/l, V[1]/l)

def closest_point_on_segment(point, a, b):
  ab = aminusb(b,a)
  ap = aminusb(point,a)

  ab_sq = dot(ab,ab)

  if ab_sq == 0:
    return a,0

  t = dot(ap, ab) / ab_sq

  t = max(0, min(1, t))

  closest = (
      a[0] + ab[0] * t,
      a[1] + ab[1] * t
  )

  return closest, t
