FB Time- (8)
	A1: Variable Set [ Name:%MSTFBtotal To:0 Recurse Variables:Off Do Maths:Off Append:Off Max Rounding Digits:3 ] If [ %MSTFBtotal !Set ]
	A2: Variable Set [ Name:%DSTFBtotal To:0 Recurse Variables:Off Do Maths:Off Append:Off Max Rounding Digits:3 ] If [ %DSTFBtotal !Set ]
	A3: Variable Set [ Name:%stop To:%TIMES - %FBstart Recurse Variables:Off Do Maths:On Append:Off Max Rounding Digits:1 ] 
	<Daily>
	A4: Variable Set [ Name:%DSTFBtotal To:%DSTFBtotal + %stop Recurse Variables:Off Do Maths:On Append:Off Max Rounding Digits:1 ] 
	<Monthly>
	A5: Variable Set [ Name:%MSTFBtotal To:%MSTFBtotal + %stop Recurse Variables:Off Do Maths:On Append:Off Max Rounding Digits:1 ] 
	A6: Array Pop [ Variable Array:%DST Position:1 To Var: ] If [ %DST1 Set ]
	<Day>
	A7: Array Push [ Variable Array:%DST Position:1 Value:%DSTFBtotal Fill Spaces:Off ] 
	A8: Array Pop [ Variable Array:%MST Position:1 To Var: ] If [ %MST1 Set ]
	<Month>
	A9: Array Push [ Variable Array:%MST Position:1 Value:%MSTFBtotal Fill Spaces:Off ] 
    
