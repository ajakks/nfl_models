## specify dicts to clean up team names per source ##
clean_team_pff_opp ={
"Arizona Cardinals":"ari",
"Atlanta Falcons":"atl",
"Baltimore Ravens":"bal",
"Buffalo Bills":"buf",
"Carolina Panthers":"car",
"Chicago Bears":"chi",
"Cincinnati Bengals":"cin",
"Cleveland Browns":"cle",
"Dallas Cowboys":"dal",
"Denver Broncos":"den",
"Detroit Lions":"det",
"Green Bay Packers":"gb",
"Houston Texans":"hou",
"Indianapolis Colts":"ind",
"Jacksonville Jaguars":"jax",
"Kansas City Chiefs":"kc",
"Los Angeles Chargers":"lac",
"Los Angeles Rams":"lar",
"Miami Dolphins":"mia",
"Minnesota Vikings":"min",
"New England Patriots":"ne",
"New Orleans Saints":"no",
"New York Giants":"nyg",
"New York Jets":"nyj",
"Oakland Raiders":"oak",
"Philadelphia Eagles":"phi",
"Pittsburgh Steelers":"pit",
"San Francisco 49ers":"sf",
"Seattle Seahawks":"sea",
"Tampa Bay Buccaneers":"tb",
"Tennessee Titans":"ten",
"Washington Redskins":"was",
"Washington Football Team":"was",
"Las Vegas Raiders":"lv",
"washington-football-team":"was",
"las-vegas-raiders":"lv"}

clean_team_pff_full = {
"arizona-cardinals":"ari",
"atlanta-falcons":"atl",
"baltimore-ravens":"bal",
"buffalo-bills":"buf",
"carolina-panthers":"car",
"chicago-bears":"chi",
"cincinnati-bengals":"cin",
"cleveland-browns":"cle",
"dallas-cowboys":"dal",
"denver-broncos":"den",
"detroit-lions":"det",
"green-bay-packers":"gb",
"houston-texans":"hou",
"indianapolis-colts":"ind",
"jacksonville-jaguars":"jax",
"kansas-city-chiefs":"kc",
"los-angeles-chargers":"lac",
"los-angeles-rams":"lar",
"miami-dolphins":"mia",
"minnesota-vikings":"min",
"new-england-patriots":"ne",
"new-orleans-saints":"no",
"new-york-giants":"nyg",
"new-york-jets":"nyj",
"oakland-raiders":"oak",
"philadelphia-eagles":"phi",
"pittsburgh-steelers":"pit",
"san-francisco-49ers":"sf",
"seattle-seahawks":"sea",
"tampa-bay-buccaneers":"tb",
"tennessee-titans":"ten",
"washington-redskins":"was",
"washington-football-team":"was",
"las-vegas-raiders":"lv"}

clean_team_pff = {"arz":"ari",
"blt":"bal",
"clv":"cle",
"hst":"hou",
"la":"lar",
"sd":"lac",
"sl":"lar"}

clean_team_pfr = {
"arz":"ari",
"crd":"ari",
"rav":"bal",
"gnb":"gb",
"htx":"hou",
"clt":"ind",
"kan":"kc",
"sdg":"lac",
"ram":"lar",
"nwe":"ne",
"nor":"no",
"rai":"oak",
"sfo":"sf",
"tam":"tb",
"oti":"ten",
"lvr":"lv"}

clean_team_pff_num = {"1":"ari",
"2":"atl",
"3":"bal",
"4":"buf",
"5":"car",
"6":"chi",
"7":"cin",
"8":"cle",
"9":"dal",
"10":"den",
"11":"det",
"12":"gb",
"13":"hou",
"14":"ind",
"15":"jax",
"16":"kc",
"17":"lac",
"18":"lar",
"19":"mia",
"20":"min",
"21":"ne",
"22":"no",
"23":"nyg",
"24":"nyj",
"25":"oak",
"26":"phi",
"27":"pit",
"28":"sf",
"29":"sea",
"30":"tb",
"31":"ten",
"32":"was"}

pos_dict = {"wlb":"lb",
"ss":"s",
"slb":"lb",
"scb":"cb",
"rolb":"lb",
"rlb":"lb",
"rilb":"lb",
"re":"dl",
"rcb":"cb",
"nt":"dl",
"mlb":"lb",
"lolb":"lb",
"llb":"lb",
"lilb":"lb",
"le":"dl",
"lcb":"cb",
"fs":"s",
"drt":"dl",
"dre":"dl",
"dlt":"dl",
"dle":"dl",
"tel":"te",
"slwr":"wr",
"rg":"ol",
"lg":"ol",
"hb":"hb",
"lwr":"wr",
"c":"ol",
"qb":"qb",
"ter":"te",
"rwr":"wr",
"fb":"fb",
"lt":"ol",
"rt":"ol",
"srwr":"wr"}

clean_team_weather={
"cardinals":"ari",
"falcons":"atl",
"ravens":"bal",
"bills":"buf",
"panthers":"car",
"bears":"chi",
"bengals":"cin",
"browns":"cle",
"cowboys":"dal",
"broncos":"den",
"lions":"det",
"packers":"gb",
"texans":"hou",
"colts":"ind",
"jaguars":"jax",
"chiefs":"kc",
"chargers":"lac",
"rams":"lar",
"dolphins":"mia",
"vikings":"min",
"patriots":"ne",
"saints":"no",
"giants":"nyg",
"jets":"nyj",
"raiders":"oak",
"eagles":"phi",
"steelers":"pit",
"49ers":"sf",
"seahawks":"sea",
"buccaneers":"tb",
"titans":"ten",
"redskins":"was",
"washington":"was"}

ht_Dict = {"6":"72",
"53":"63",
"54":"64",
"55":"65",
"56":"66",
"57":"67",
"58":"68",
"59":"69",
"60":"72",
"61":"73",
"62":"74",
"63":"75",
"64":"76",
"65":"77",
"66":"78",
"67":"79",
"68":"80",
"69":"81",
"510":"70",
"511":"71",
"5’10":"70",
"5’11":"71",
"5’6":"66",
"5’7":"67",
"5’8":"68",
"5’9":"69",
"5-0":"60",
"5-1":"61",
"5-10":"70",
"5-101":"70",
"5-11":"71",
"5-14":"70",
"5-171":"70",
"5-2":"62",
"5-24":"62",
"5-3":"63",
"5-4":"64",
"5-5":"65",
"5-6":"66",
"5-7":"67",
"5-7.5":"67",
"5-8":"68",
"5-8.5":"68",
"5-9":"69",
"5-9.5":"69",
"6-":"72",
"6 0 - 175 lbs.":"72",
"6 0 - 182 lbs.":"72",
"6 0 - 185 lbs.":"72",
"6 0 - 186 lbs.":"72",
"6 0 - 188 lbs.":"72",
"6 0 - 192 lbs.":"72",
"6 0 - 197 lbs.":"72",
"6 0 - 199 lbs.":"72",
"6 0 - 202 lbs.":"72",
"6 0 - 208 lbs.":"72",
"6 0 - 218 lbs.":"72",
"6 0 - 220 lbs.":"72",
"6 0 - 225 lbs.":"72",
"6 0 - 235 lbs.":"72",
"6 0 - 250 lbs.":"72",
"6 0 - 270 lbs.":"72",
"6 1 - 165 lbs.":"73",
"6 1 - 175 lbs.":"73",
"6 1 - 190 lbs.":"73",
"6 1 - 195 lbs.":"73",
"6 1 - 210 lbs.":"73",
"6 1 - 219 lbs.":"73",
"6 1 - 225 lbs.":"73",
"6 1 - 230 lbs.":"73",
"6 1 - 243 lbs.":"73",
"6 1 - 287 lbs.":"73",
"6 2 - 180 lbs.":"74",
"6 2 - 185 lbs.":"74",
"6 2 - 195 lbs.":"74",
"6 2 - 196 lbs.":"74",
"6 2 - 210 lbs.":"74",
"6 2 - 218 lbs.":"74",
"6 2 - 230 lbs.":"74",
"6 2 - 250 lbs.":"74",
"6 2 - 280 lbs.":"74",
"6 2 - 285 lbs.":"74",
"6 2 - 301 lbs.":"74",
"6 3 - 185 lbs.":"75",
"6 3 - 195 lbs.":"75",
"6 3 - 201 lbs.":"75",
"6 3 - 205 lbs.":"75",
"6 3 - 215 lbs.":"75",
"6 3 - 229 lbs.":"75",
"6 3 - 233 lbs.":"75",
"6 3 - 236 lbs.":"75",
"6 3 - 255 lbs.":"75",
"6 3 - 300 lbs.":"75",
"6 3 - 305 lbs.":"75",
"6 4 - 210 lbs.":"76",
"6 4 - 228 lbs.":"76",
"6 4 - 232 lbs.":"76",
"6 4 - 259 lbs.":"76",
"6 4 - 260 lbs.":"76",
"6 4 - 270 lbs.":"76",
"6 4 - 280 lbs.":"76",
"6 4 - 281 lbs.":"76",
"6 4 - 285 lbs.":"76",
"6 4 - 318 lbs.":"76",
"6 4 - 346 lbs.":"76",
"6 4 - 360 lbs.":"76",
"6 5 - 250 lbs.":"77",
"6 5 - 265 lbs.":"77",
"6 5 - 290 lbs.":"77",
"6 5 - 295 lbs.":"77",
"6 5 - 301 lbs.":"77",
"6 5 - 325 lbs.":"77",
"6 5 - 330 lbs.":"77",
"6 5 - 350 lbs.":"77",
"6 6 - 230 lbs.":"78",
"6 6 - 250 lbs.":"78",
"6 6 - 305 lbs.":"78",
"6 9 - 312 lbs.":"81",
"6 9 - 315 lbs.":"81",
"6*1":"73",
"6;0":"72",
"6’0":"72",
"6’1":"73",
"6’2":"74",
"6’3":"75",
"6’4":"76",
"6’5":"77",
"6’6":"78",
"6-0":"72",
"6--0":"72",
"6-1":"73",
"6-10":"82",
"6-11":"83",
"6-2":"73",
"6-225":"72",
"6-3":"75",
"6-4":"76",
"6-5":"77",
"6-6":"78",
"6-7":"79",
"6-8":"80",
"6-9":"81",
"7-0":"84",
"7-1":"85",
"4-11":"59",
"4-11":"59",
"5-1":"61",
"5/2":"62",
"5-2":"62",
"5-24":"62",
"5/3":"63",
"5/4":"64",
"5-4":"64",
"5'4":"64",
"5/5":"65",
"5'5":"65",
"5-5":"65",
"5'5":"65",
"5/6":"66",
"5-6":"66",
"5'6":"66",
"5/7":"67",
"5'7":"67",
"5-7":"67",
"5--7":"67",
"5'7":"67",
"5-7.5":"67",
"58":"68",
"58":"68",
"5/8":"68",
"5'8":"68",
"5-8":"68",
"5'8":"68",
"5-8.5":"68",
"5/9":"69",
"5'9":"69",
"5'9''":"69",
"5-9":"69",
"5'9":"69",
"5-9.5":"69",
"5-910":"69",
"5/10":"70",
"5'10":"70",
"5-10":"70",
"5'10":"70",
"5-100":"70",
"5' 11":"71",
"5/11":"71",
"5'11":"71",
"5'11''":"71",
"5-11":"71",
"5'11":"71",
"5-14":"71",
"6-":"72",
"6'0":"72",
"6'0''":"72",
"6-0":"72",
"6'0":"72",
"6*1":"73",
"6/1":"73",
"6/10":"73",
"6'1":"73",
"6-1":"73",
"6'1":"73",
"6-10":"73",
"6-11":"73",
"6-12":"73",
"6-13":"73",
"6-14":"73",
"6-15":"73",
"6-16":"73",
"6-17":"73",
"6-18":"73",
"6-19":"73",
"6/2":"74",
"6/20":"74",
"6'2":"74",
"6-2":"74",
"6'2":"74",
"6-20":"74",
"6-21":"74",
"6-22":"74",
"6-225":"74",
"6-23":"74",
"6-24":"74",
"6-25":"74",
"6/3":"75",
"6'3":"75",
"6-3":"75",
"6'3":"75",
"6-36-1":"75",
"6/4":"76",
"6'4":"76",
"6-4":"76",
"6'4":"76",
"6/5":"77",
"6'5":"77",
"6-5":"77",
"6'5":"77",
"6/6":"78",
"6'6":"78",
"6-6":"78",
"6'6":"78",
"6/7":"79",
"6-7":"79",
"6/8":"80",
"6-8":"80",
"6'8":"80",
"6-9":"81",
"6/9":"84",
"5-Jun":"77",
"Jun-31":"72",
"May-00":"60",
"Jun-00":"72",
"Jun-00":"72",
"Jun-00":"72",
"5-Mar":"63",
"11-Apr":"59",
"2-May":"62",
"3-May":"63",
"4-May":"64",
"5-May":"65",
"6-May":"66",
"7-May":"67",
"7-May":"67",
"8-May":"68",
"8-May":"68",
"9-May":"69",
"9-May":"69",
"10-May":"70",
"10-May":"70",
"11-May":"71",
"11-May":"71",
"18-May":"68",
"1-Jun":"73",
"1-Jun":"73",
"2-Jun":"74",
"2-Jun":"74",
"3-Jun":"75",
"3-Jun":"75",
"4-Jun":"76",
"4-Jun":"76",
"5-Jun":"77",
"5-Jun":"77",
"6-Jun":"78",
"7-Jun":"79",
"8-Jun":"80",
"11-Jun":"83",
"5/1/2000":"70",
"6/1/2000":"73",
"6/1/2000":"73",
"5/2/2019":"62",
"5/3/2019":"63",
"5/5/2019":"65",
"5-May":"65",
"5/6/2019":"66",
"6-May":"66",
"5/7/2019":"67",
"7-May":"67",
"8-May":"68",
"5/8/2019":"68",
"5/9/2019":"69",
"9-May":"69",
"5/9/2019":"69",
"10-May":"70",
"5/10/2019":"70",
"5/11/2019":"71",
"11-May":"71",
"5/14/2019":"71",
"1-Jun":"73",
"6/1/2019":"73",
"6/2/2019":"74",
"2-Jun":"74",
"6/3/2019":"75",
"3-Jun":"75",
"6/4/2019":"76",
"4-Jun":"76",
"6/4/2019":"76",
"6/5/2019":"77",
"5-Jun":"77",
"6/6/2019":"78",
"6-Jun":"78",
"6/7/2019":"79",
"7-Jun":"79",
"6/8/2019":"80",
"8-Jun":"80",
"6/15/2019":"73",
"6/25/2019":"74",
"5-10.25":"70.5",
"5-10.5":"70.5",
"5-11.25":"71.5",
"5-11.5":"71.5",
"5-3.5":"63.5",
"5-4.25":"64",
"5-4.5":"64.5",
"5-6.5":"66.5",
"5-7.25":"67",
"5-7.5":"67.5",
"5-8.25":"68",
"5-8.5":"68.5",
"5-9.25":"69",
"5-9.5":"69.5",
"6-0.25":"72",
"6-0.5":"72.5",
"6-0.5":"72.5",
"6-1.25":"73",
"6-1.5":"73.5",
"6-2.25":"74",
"6-2.5":"74.5",
"6-2.5":"74.5",
"6-3.25":"75",
"6-3.5":"75.5",
"6-3.5":"75.5",
"6-4.25":"76",
"6-4.25":"76",
"6-4.5":"76.5",
"6-4.5":"76.5",
"6-5.5":"77.5",
"6-5.5":"77.5",
"6-6.25":"78",
"6-6.5":"78.5",
"6-6.5":"78.5",
"6-6.5 ":"78.5",
"6-7.5":"79.5"}