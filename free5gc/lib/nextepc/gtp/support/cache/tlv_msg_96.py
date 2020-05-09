ies = []
ies.append({ "ie_type" : "Cause", "ie_value" : "Cause", "presence" : "M", "instance" : "0", "comment" : ""})
ies.append({ "ie_type" : "Bearer Context", "ie_value" : "Bearer Contexts", "presence" : "M", "instance" : "0", "comment" : "All the bearer contexts included in the corresponding Create Bearer Request shall be included. Several IEs with this type and instance value shall be included on the S4/S11, S5/S8 and S2a/S2b interfaces as necessary to represent a list of Bearers."})
ies.append({ "ie_type" : "Recovery", "ie_value" : "Recovery", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included on the S4/S11, S5/S8 and S2a/S2b interfaces if contacting the peer for the first time"})
ies.append({ "ie_type" : "FQ-CSID", "ie_value" : "MME-FQ-CSID", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included by the MME on the S11 interfaceand shall be forwarded by the SGW on the S5/S8 interfaces according to the requirements in 3GPP TS 23.007 [17]."})
ies.append({ "ie_type" : "FQ-CSID", "ie_value" : "ePDG-FQ-CSID", "presence" : "C", "instance" : "2", "comment" : "This IE shall be included by the ePDG on the S2b interface according to the requirements in 3GPP TS 23.007 [17]."})
ies.append({ "ie_type" : "FQ-CSID", "ie_value" : "TWAN-FQ-CSID", "presence" : "C", "instance" : "3", "comment" : "This IE shall be included by the TWAN on the S2a interface according to the requirements in 3GPP TS 23.007 [17]."})
ies.append({ "ie_type" : "PCO", "ie_value" : "Protocol Configuration Options", "presence" : "C", "instance" : "0", "comment" : "If the UE includes the PCO IE, then the MME/SGSN shall copy the content of this IE transparently from the PCO IE included by the UE. If the SGW receives PCO from MME/SGSN, SGW shall forward it to the PGW."})
ies.append({ "ie_type" : "UE Time Zone", "ie_value" : "UE Time Zone", "presence" : "O", "instance" : "0", "comment" : "This IE is optionally included by the MME on the S11 interface or by the SGSN on the S4 interface. "})
ies.append({ "ie_type" : "ULI", "ie_value" : "User Location Information", "presence" : "CO", "instance" : "0", "comment" : "This IE shall be included by the MME on the S11 interface or by the SGSN on the S4 interface. The CGI/SAI shall be included by SGSN and the ECGI shall be included by MME. See NOTE 1."})
ies.append({ "ie_type" : "TWAN Identifier", "ie_value" : "TWAN Identifier", "presence" : "CO", "instance" : "0", "comment" : "This IE shall be included by the TWAN on the S2a interface as specified in 3GPP TS 23.402 [45]. "})
ies.append({ "ie_type" : "Overload Control Information", "ie_value" : "MME/S4-SGSN's Overload Control Information", "presence" : "O", "instance" : "0", "comment" : "During an overload condition, the MME/S4-SGSN may include this IE on the S11/S4 interface if the overload control feature is supported by the MME/S4-SGSN and is activated for the PLMN to which the PGW belongs (see clause 12.3.11).When present, the MME/S4-SGSN shall provide only one instance of this IE, representing its overload information."})
ies.append({ "ie_type" : "Overload Control Information", "ie_value" : "SGW's Overload Control Information", "presence" : "O", "instance" : "1", "comment" : "During an overload condition, the SGW may include this IE over the S5/S8 interface if the overload control feature is supported by the SGW and is activated for the PLMN to which the PGW belongs (see clause 12.3.11).When present, the SGW shall provide only one instance of this IE, representing its overload information."})
ies.append({ "ie_type" : "Presence Reporting Area Information", "ie_value" : "Presence Reporting Area Information", "presence" : "CO", "instance" : "0", "comment" : "The MME/SGSN shall include this IE on S11/S4 if the PGW/PCRF has requested to start reporting changes of UE presence in a Presence Reporting Area in the corresponding Create Bearer Request message and the MME/SGSN supports such reporting. The MME/SGSN shall then indicate whether the UE is inside or outside the Presence Reporting Area.The SGW shall include this IE on S5/S8 if it receives the Presence Reporting Area Information from the MME/SGSN."})
ies.append({ "ie_type" : "IP Address", "ie_value" : "MME/S4-SGSN Identifier", "presence" : "CO", "instance" : "0", "comment" : "If the overload control feature is supported by the MME/S4-SGSN and is activated for the PLMN to which the PGW belongs (see subclause 12.3.11), the MME/S4-SGSN shall include this IE on the S11/S4 interface if the PGW has not been updated with the identity of the currently serving MME/S4-SGSN, i.e. if no other message carrying MME/S4-SGSN identity has been sent to the PGW during/after an inter-MME/S4-SGSN intra-SGW mobility procedure."})
ies.append({ "ie_type" : "Overload Control Information", "ie_value" : "TWAN/ePDG's Overload Control Information", "presence" : "O", "instance" : "2", "comment" : "During an overload condition, the TWAN/ePDG may include this IE over the S2a/S2b interface if the overload control feature is supported by the TWAN/ePDG and is activated for the PLMN to which the PGW belongs (see clause 12.3.11).When present, the TWAN/ePDG shall provide only one instance of this IE, representing its overload information."})
ies.append({ "ie_type" : "TWAN Identifier", "ie_value" : "WLAN Location Information", "presence" : "CO", "instance" : "1", "comment" : "The ePDG shall include this IE on the S2b interface if the WLAN Location Information is available. "})
ies.append({ "ie_type" : "TWAN Identifier Timestamp", "ie_value" : "WLAN Location Timestamp", "presence" : "CO", "instance" : "1", "comment" : "The ePDG shall include this IE on the S2b interface, if the WLAN Location Timestamp is available. "})
ies.append({ "ie_type" : "Port Number", "ie_value" : "UE UDP Port", "presence" : "CO", "instance" : "0", "comment" : "The ePDG shall include this IE on the S2b interface if NAT is detected."})
ies.append({ "ie_type" : "F-Container", "ie_value" : "NBIFOM Container", "presence" : "CO", "instance" : "0", "comment" : "This IE shall be included on the S11/S4 or S2a/S2b interfaces if the MME/S4-SGSN or the TWAN/ePDG receives a NBIFOM Container from the UE as specified in 3GPP TS 24.161 73]. The Container Type shall be set to 4."})
ies.append({ "ie_type" : "Port Number", "ie_value" : "UE TCP Port", "presence" : "CO", "instance" : "1", "comment" : "The ePDG shall include this IE on the S2b interface if NAT is detected and the TCP encapsulation is used."})
msg_list[key]["ies"] = ies
