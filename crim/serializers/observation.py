from crim.models.observation import CRIMObservation
from rest_framework import serializers

from crim.models.person import CRIMPerson
from crim.models.piece import CRIMPiece


class CRIMPersonObservationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimperson-detail', lookup_field='person_id')

    class Meta:
        model = CRIMPerson
        fields = (
            'url',
            'name',
        )


class CRIMPieceObservationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimpiece-detail', lookup_field='piece_id')

    class Meta:
        model = CRIMPiece
        fields = (
            'url',
        )


class CRIMObservationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimobservation-detail')
    observer = CRIMPersonObservationSerializer(read_only=True)
    piece = CRIMPieceObservationSerializer(read_only=True)

    class Meta:
        model = CRIMObservation
        fields = (
            'url',
            'observer',
            'piece',
            'ema',
            'mt_cf_voices',
            'mt_cf_dur',
            'mt_cf_mel',
            'mt_sog_voices',
            'mt_sog_dur',
            'mt_sog_mel',
            'mt_sog_ostinato',
            'mt_sog_periodic',
            'mt_csog_voices',
            'mt_csog_dur',
            'mt_csog_mel',
            'mt_cd_voices',
            'mt_fg_voices',
            'mt_fg_periodic',
            'mt_fg_strict',
            'mt_fg_flexed',
            'mt_fg_sequential',
            'mt_fg_inverted',
            'mt_fg_retrograde',
            'mt_fg_int',
            'mt_fg_tint',
            'mt_id_voices',
            'mt_id_strict',
            'mt_id_flexed',
            'mt_id_flt',
            'mt_id_invertible',
            'mt_id_int',
            'mt_id_tint',
            'mt_pe_voices',
            'mt_pe_strict',
            'mt_pe_flexed',
            'mt_pe_flt',
            'mt_pe_sequential',
            'mt_pe_added',
            'mt_pe_invertible',
            'mt_pe_int',
            'mt_pe_tint',
            'mt_nid_voices',
            'mt_nid_strict',
            'mt_nid_flexed',
            'mt_nid_flt',
            'mt_nid_sequential',
            'mt_nid_invertible',
            'mt_nid_int',
            'mt_nid_tint',
            'mt_hr_voices',
            'mt_hr_simple',
            'mt_hr_staggered',
            'mt_hr_sequential',
            'mt_hr_fauxbourdon',
            'mt_cad_cantizans',
            'mt_cad_tenorizans',
            'mt_cad_authentic',
            'mt_cad_phrygian',
            'mt_cad_plagal',
            'mt_cad_tone',
            'mt_cad_dtv',
            'mt_cad_dti',
            'mt_int_voices',
            'mt_int_p6',
            'mt_int_p3',
            'mt_int_c35',
            'mt_int_c83',
            'mt_int_c65',
            'mt_fp_comment',
            'mt_fp_ir',
            'mt_fp_range',
            'remarks',
            'created',
            'updated',
        )
