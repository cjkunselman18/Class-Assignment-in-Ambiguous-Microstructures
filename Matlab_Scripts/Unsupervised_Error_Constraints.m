function [c, ceq] = Unsupervised_Error_Constraints(x,agreement_rates)

e1 = x(1);
e2 = x(2);
e3 = x(3);
e4 = x(4);
e5 = x(5);
e12 = x(6);
e13 = x(7);
e14 = x(8);
e15 = x(9);
e23 = x(10);
e24 = x(11);
e25 = x(12);
e34 = x(13);
e35 = x(14);
e45 = x(15);
e123 = x(16);
e124 = x(17);
e125 = x(18);
e134 = x(19);
e135 = x(20);
e145 = x(21);
e234 = x(22);
e235 = x(23);
e245 = x(24);
e345 = x(25);
e1234 = x(26);
e1235 = x(27);
e1245 = x(28);
e1345 = x(29);
e2345 = x(30);
e12345 = x(31);


a12 = agreement_rates(1)/52;
a13 = agreement_rates(2)/52;
a14 = agreement_rates(3)/52;
a15 = agreement_rates(4)/52;
a23 = agreement_rates(5)/52;
a24 = agreement_rates(6)/52;
a25 = agreement_rates(7)/52;
a34 = agreement_rates(8)/52;
a35 = agreement_rates(9)/52;
a45 = agreement_rates(10)/52;
a123 = agreement_rates(11)/52;
a124 = agreement_rates(12)/52;
a125 = agreement_rates(13)/52;
a134 = agreement_rates(14)/52;
a135 = agreement_rates(15)/52;
a145 = agreement_rates(16)/52;
a234 = agreement_rates(17)/52;
a235 = agreement_rates(18)/52;
a245 = agreement_rates(19)/52;
a345 = agreement_rates(20)/52;
a1234 = agreement_rates(21)/52;
a1235 = agreement_rates(22)/52;
a1245 = agreement_rates(23)/52;
a1345 = agreement_rates(24)/52;
a2345 = agreement_rates(25)/52;
a12345 = agreement_rates(26)/52;

ceq = [1 - e1 - e2 + 2*e12 - a12,
     1 - e1 - e3 + 2*e13 - a13,
     1 - e1 - e4 + 2*e14 - a14,
     1 - e1 - e5 + 2*e15 - a15,
     1 - e2 - e3 + 2*e23 - a23,
     1 - e2 - e4 + 2*e24 - a24,
     1 - e2 - e5 + 2*e25 - a25,
     1 - e3 - e4 + 2*e34 - a34,
     1 - e3 - e5 + 2*e35 - a35,
     1 - e4 - e5 + 2*e45 - a45,
     1 - e1 - e2 - e3 + e12 + e13 + e23 - a123,
     1 - e1 - e2 - e4 + e12 + e14 + e24 - a124,
     1 - e1 - e2 - e5 + e12 + e15 + e25 - a125,
     1 - e1 - e3 - e4 + e13 + e14 + e34 - a134,
     1 - e1 - e3 - e5 + e13 + e15 + e35 - a135,
     1 - e1 - e4 - e5 + e14 + e15 + e45 - a145,
     1 - e2 - e3 - e4 + e23 + e24 + e34 - a234,
     1 - e2 - e3 - e5 + e23 + e25 + e35 - a235,
     1 - e2 - e4 - e5 + e24 + e25 + e45 - a245,
     1 - e3 - e4 - e5 + e34 + e35 + e45 - a345,
     1 - e1 - e2 - e3 - e4 + e12 + e13 + e14 + e23 + e24 + e34 - e123 - e124 - e134 - e234 + 2*e1234 - a1234,
     1 - e1 - e2 - e3 - e5 + e12 + e13 + e15 + e23 + e25 + e35 - e123 - e125 - e135 - e235 + 2*e1235 - a1235,
     1 - e1 - e2 - e4 - e5 + e12 + e14 + e15 + e24 + e25 + e45 - e124 - e125 - e145 - e245 + 2*e1245 - a1245,
     1 - e1 - e3 - e4 - e5 + e13 + e14 + e15 + e34 + e35 + e45 - e134 - e135 - e145 - e345 + 2*e1345 - a1345,
     1 - e2 - e3 - e4 - e5 + e23 + e24 + e25 + e34 + e35 + e45 - e234 - e235 - e245 - e345 + 2*e2345 - a2345,
     1 - e1 - e2 - e3 - e4 - e5 + e12 + e13 + e14 + e15 + e23 + e24 + e25 + e34 + e35 + e45 - e123 - e124 - e125 - e134 - e135 - e145 - e234 - e235 - e245 - e345 + e1234 + e1235 + e1245 + e1345 + e2345 - a12345];
 
 c = [e12 - min([e1,e2]),
      e13 - min([e1,e3]),
      e14 - min([e1,e4]),
      e15 - min([e1,e5]),
      e23 - min([e2,e3]),
      e24 - min([e2,e4]),
      e25 - min([e2,e5]),
      e34 - min([e3,e4]),
      e35 - min([e3,e5]),
      e45 - min([e4,e5]),
      e123 - min([e12,e13,e23]),
      e124 - min([e12,e14,e24]),
      e125 - min([e12,e15,e25]),
      e134 - min([e13,e14,e34]),
      e135 - min([e13,e15,e35]),
      e145 - min([e14,e15,e45]),
      e234 - min([e23,e24,e34]),
      e235 - min([e23,e25,e35]),
      e245 - min([e24,e25,e45]),
      e345 - min([e34,e35,e45]),
      e1234 - min([e123,e124,e134,e234]),
      e1235 - min([e123,e125,e135,e235]),
      e1245 - min([e124,e125,e145,e245]),
      e1345 - min([e134,e135,e145,e345]),
      e2345 - min([e234,e235,e245,e345]),
      min([e1,e2,e3,e4,e5]) - .5,
      e12345 - min([e1234,e1235,e1245,e1345,e2345])];
  
 


end
