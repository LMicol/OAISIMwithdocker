/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "NGAP-IEs"
 * 	found in "../support/r14.4.0/38413-e40.asn"
 * 	`asn1c -pdu=all -fcompound-names -findirect-choice -fno-include-deps`
 */

#ifndef	_NGAP_Dynamic5QIDescriptor_H_
#define	_NGAP_Dynamic5QIDescriptor_H_


#include <asn_application.h>

/* Including external dependencies */
#include "NGAP_PriorityLevelQos.h"
#include "NGAP_PacketDelayBudget.h"
#include "NGAP_PacketErrorRate.h"
#include "NGAP_DelayCritical.h"
#include "NGAP_AveragingWindow.h"
#include "NGAP_MaximumDataBurstVolume.h"
#include <constr_SEQUENCE.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Forward declarations */
struct NGAP_ProtocolExtensionContainer;

/* NGAP_Dynamic5QIDescriptor */
typedef struct NGAP_Dynamic5QIDescriptor {
	NGAP_PriorityLevelQos_t	 priorityLevelQos;
	NGAP_PacketDelayBudget_t	 packetDelayBudget;
	NGAP_PacketErrorRate_t	 packetErrorRate;
	NGAP_DelayCritical_t	*delayCritical;	/* OPTIONAL */
	NGAP_AveragingWindow_t	*averagingWindow;	/* OPTIONAL */
	NGAP_MaximumDataBurstVolume_t	*maximumDataBurstVolume;	/* OPTIONAL */
	struct NGAP_ProtocolExtensionContainer	*iE_Extensions;	/* OPTIONAL */
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} NGAP_Dynamic5QIDescriptor_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_NGAP_Dynamic5QIDescriptor;
extern asn_SEQUENCE_specifics_t asn_SPC_NGAP_Dynamic5QIDescriptor_specs_1;
extern asn_TYPE_member_t asn_MBR_NGAP_Dynamic5QIDescriptor_1[7];

#ifdef __cplusplus
}
#endif

#endif	/* _NGAP_Dynamic5QIDescriptor_H_ */
#include <asn_internal.h>
