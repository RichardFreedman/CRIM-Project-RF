"""
Django settings for crim project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from crim.settings_production import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!si#%r2x)6yu*dlxw#rx#)1w1gm+1jkz+zwr&_w2-ldr*9js%d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '159.65.177.99']


# Application definition

INSTALLED_APPS = [
    'crim',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'bootstrap_pagination',
    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crim.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crim.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:m'
DATETIME_FORMAT = 'Y-m-d, H:m'
SHORT_DATETIME_FORMAT = 'Y-m-d, H:m'

USE_TZ = True

LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/'

# Make it acceptable for users to leave off a slash in URLs
APPEND_SLASH = True

SITE_ID = 2

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'crim/static')

SOLR_FACET_FIELDS = [
    'observer_s',
    'rt_q_b',
    'rt_q_x_b',
    'rt_q_monnayage_b',
    'rt_tm_b',
    'rt_tm_snd_b',
    'rt_tm_minv_b',
    'rt_tm_retrograde_b',
    'rt_tm_ms_b',
    'rt_tm_transposed_b',
    'rt_tm_invertible_b',
    'rt_tnm_b',
    'rt_tnm_embellished_b',
    'rt_tnm_reduced_b',
    'rt_tnm_amplified_b',
    'rt_tnm_truncated_b',
    'rt_tnm_ncs_b',
    'rt_tnm_ocs_b',
    'rt_tnm_ocst_b',
    'rt_tnm_nc_b',
    'rt_nm_b',
    'rt_om_b',
    'remarks_t',
    'created_dt',
    'updated_dt',
    'status_b',
    'model_observer_s',
    'model_ema_s',
    'model_mt_cf_b',
    'model_mt_cf_voices_ss',
    'model_mt_cf_dur_b',
    'model_mt_cf_mel_b',
    'model_mt_sog_b',
    'model_mt_sog_voices_ss',
    'model_mt_sog_dur_b',
    'model_mt_sog_mel_b',
    'model_mt_sog_ostinato_b',
    'model_mt_sog_periodic_b',
    'model_mt_csog_b',
    'model_mt_csog_voices_ss',
    'model_mt_csog_dur_b',
    'model_mt_csog_mel_b',
    'model_mt_cd_b',
    'model_mt_cd_voices_ss',
    'model_mt_fg_b',
    'model_mt_fg_voices_ss',
    'model_mt_fg_periodic_b',
    'model_mt_fg_strict_b',
    'model_mt_fg_flexed_b',
    'model_mt_fg_sequential_b',
    'model_mt_fg_inverted_b',
    'model_mt_fg_retrograde_b',
    'model_mt_fg_int_s',
    'model_mt_fg_tint_s',
    'model_mt_id_b',
    'model_mt_id_voices_ss',
    'model_mt_id_strict_b',
    'model_mt_id_flexed_b',
    'model_mt_id_flt_b',
    'model_mt_id_invertible_b',
    'model_mt_id_int_s',
    'model_mt_id_tint_s',
    'model_mt_pe_b',
    'model_mt_pe_voices_ss',
    'model_mt_pe_strict_b',
    'model_mt_pe_flexed_b',
    'model_mt_pe_flt_b',
    'model_mt_pe_sequential_b',
    'model_mt_pe_added_b',
    'model_mt_pe_invertible_b',
    'model_mt_pe_int_s',
    'model_mt_pe_tint_s',
    'model_mt_nid_b',
    'model_mt_nid_voices_ss',
    'model_mt_nid_strict_b',
    'model_mt_nid_flexed_b',
    'model_mt_nid_flt_b',
    'model_mt_nid_sequential_b',
    'model_mt_nid_invertible_b',
    'model_mt_nid_int_s',
    'model_mt_nid_tint_s',
    'model_mt_hr_b',
    'model_mt_hr_voices_ss',
    'model_mt_hr_simple_b',
    'model_mt_hr_staggered_b',
    'model_mt_hr_sequential_b',
    'model_mt_hr_fauxbourdon_b',
    'model_mt_cad_b',
    'model_mt_cad_cantizans_s',
    'model_mt_cad_tenorizans_s',
    'model_mt_cad_authentic_b',
    'model_mt_cad_phrygian_b',
    'model_mt_cad_plagal_b',
    'model_mt_cad_tone_s',
    'model_mt_cad_dtv_s',
    'model_mt_cad_dti_s',
    'model_mt_int_b',
    'model_mt_int_voices_ss',
    'model_mt_int_p6_b',
    'model_mt_int_p3_b',
    'model_mt_int_c35_b',
    'model_mt_int_c83_b',
    'model_mt_int_c65_b',
    'model_mt_fp_b',
    'model_mt_fp_comment_t',
    'model_mt_fp_ir_b',
    'model_mt_fp_range_s',
    'model_remarks_t',
    'model_created_dt',
    'model_updated_dt',
    'model_status_b',
    'model_piece_id_s',
    'model_title_s',
    'model_mass_s',
    'model_composer_s',
    'model_genre_s',
    'model_date_i',
    'model_pdf_links_ss',
    'model_mei_links_ss',
    'model_remarks_t',
    'derivative_observer_s',
    'derivative_ema_s',
    'derivative_mt_cf_b',
    'derivative_mt_cf_voices_ss',
    'derivative_mt_cf_dur_b',
    'derivative_mt_cf_mel_b',
    'derivative_mt_sog_b',
    'derivative_mt_sog_voices_ss',
    'derivative_mt_sog_dur_b',
    'derivative_mt_sog_mel_b',
    'derivative_mt_sog_ostinato_b',
    'derivative_mt_sog_periodic_b',
    'derivative_mt_csog_b',
    'derivative_mt_csog_voices_ss',
    'derivative_mt_csog_dur_b',
    'derivative_mt_csog_mel_b',
    'derivative_mt_cd_b',
    'derivative_mt_cd_voices_ss',
    'derivative_mt_fg_b',
    'derivative_mt_fg_voices_ss',
    'derivative_mt_fg_periodic_b',
    'derivative_mt_fg_strict_b',
    'derivative_mt_fg_flexed_b',
    'derivative_mt_fg_sequential_b',
    'derivative_mt_fg_inverted_b',
    'derivative_mt_fg_retrograde_b',
    'derivative_mt_fg_int_s',
    'derivative_mt_fg_tint_s',
    'derivative_mt_id_b',
    'derivative_mt_id_voices_ss',
    'derivative_mt_id_strict_b',
    'derivative_mt_id_flexed_b',
    'derivative_mt_id_flt_b',
    'derivative_mt_id_invertible_b',
    'derivative_mt_id_int_s',
    'derivative_mt_id_tint_s',
    'derivative_mt_pe_b',
    'derivative_mt_pe_voices_ss',
    'derivative_mt_pe_strict_b',
    'derivative_mt_pe_flexed_b',
    'derivative_mt_pe_flt_b',
    'derivative_mt_pe_sequential_b',
    'derivative_mt_pe_added_b',
    'derivative_mt_pe_invertible_b',
    'derivative_mt_pe_int_s',
    'derivative_mt_pe_tint_s',
    'derivative_mt_nid_b',
    'derivative_mt_nid_voices_ss',
    'derivative_mt_nid_strict_b',
    'derivative_mt_nid_flexed_b',
    'derivative_mt_nid_flt_b',
    'derivative_mt_nid_sequential_b',
    'derivative_mt_nid_invertible_b',
    'derivative_mt_nid_int_s',
    'derivative_mt_nid_tint_s',
    'derivative_mt_hr_b',
    'derivative_mt_hr_voices_ss',
    'derivative_mt_hr_simple_b',
    'derivative_mt_hr_staggered_b',
    'derivative_mt_hr_sequential_b',
    'derivative_mt_hr_fauxbourdon_b',
    'derivative_mt_cad_b',
    'derivative_mt_cad_cantizans_s',
    'derivative_mt_cad_tenorizans_s',
    'derivative_mt_cad_authentic_b',
    'derivative_mt_cad_phrygian_b',
    'derivative_mt_cad_plagal_b',
    'derivative_mt_cad_tone_s',
    'derivative_mt_cad_dtv_s',
    'derivative_mt_cad_dti_s',
    'derivative_mt_int_b',
    'derivative_mt_int_voices_ss',
    'derivative_mt_int_p6_b',
    'derivative_mt_int_p3_b',
    'derivative_mt_int_c35_b',
    'derivative_mt_int_c83_b',
    'derivative_mt_int_c65_b',
    'derivative_mt_fp_b',
    'derivative_mt_fp_comment_t',
    'derivative_mt_fp_ir_b',
    'derivative_mt_fp_range_s',
    'derivative_remarks_t',
    'derivative_created_dt',
    'derivative_updated_dt',
    'derivative_status_b',
    'derivative_piece_id_s',
    'derivative_title_s',
    'derivative_mass_s',
    'derivative_composer_s',
    'derivative_genre_s',
    'derivative_date_i',
    'derivative_pdf_links_ss',
    'derivative_mei_links_ss',
    'derivative_remarks_t',
]
# The mapping between the search form parameters and the
# Solr fields.
SEARCH_PARAM_MAP = {
    'q': 'q',
    'observer': 'observer_s',
    'rt-q': 'rt_q_b',
    'rt-q-x': 'rt_q_x_b',
    'rt-q-monnayage': 'rt_q_monnayage_b',
    'rt-tm': 'rt_tm_b',
    'rt-tm-snd': 'rt_tm_snd_b',
    'rt-tm-minv': 'rt_tm_minv_b',
    'rt-tm-retrograde': 'rt_tm_retrograde_b',
    'rt-tm-ms': 'rt_tm_ms_b',
    'rt-tm-transposed': 'rt_tm_transposed_b',
    'rt-tm-invertible': 'rt_tm_invertible_b',
    'rt-tnm': 'rt_tnm_b',
    'rt-tnm-embellished': 'rt_tnm_embellished_b',
    'rt-tnm-reduced': 'rt_tnm_reduced_b',
    'rt-tnm-amplified': 'rt_tnm_amplified_b',
    'rt-tnm-truncated': 'rt_tnm_truncated_b',
    'rt-tnm-ncs': 'rt_tnm_ncs_b',
    'rt-tnm-ocs': 'rt_tnm_ocs_b',
    'rt-tnm-ocst': 'rt_tnm_ocst_b',
    'rt-tnm-nc': 'rt_tnm_nc_b',
    'rt-nm': 'rt_nm_b',
    'rt-om': 'rt_om_b',
    'remarks': 'remarks_t',
    'created': 'created_dt',
    'updated': 'updated_dt',
    'status': 'status_b',
    'model-observer': 'model_observer_s',
    'model-ema': 'model_ema_s',
    'model-mt-cf': 'model_mt_cf_b',
    'model-mt-cf-voices': 'model_mt_cf_voices_ss',
    'model-mt-cf-dur': 'model_mt_cf_dur_b',
    'model-mt-cf-mel': 'model_mt_cf_mel_b',
    'model-mt-sog': 'model_mt_sog_b',
    'model-mt-sog-voices': 'model_mt_sog_voices_ss',
    'model-mt-sog-dur': 'model_mt_sog_dur_b',
    'model-mt-sog-mel': 'model_mt_sog_mel_b',
    'model-mt-sog-ostinato': 'model_mt_sog_ostinato_b',
    'model-mt-sog-periodic': 'model_mt_sog_periodic_b',
    'model-mt-csog': 'model_mt_csog_b',
    'model-mt-csog-voices': 'model_mt_csog_voices_ss',
    'model-mt-csog-dur': 'model_mt_csog_dur_b',
    'model-mt-csog-mel': 'model_mt_csog_mel_b',
    'model-mt-cd': 'model_mt_cd_b',
    'model-mt-cd-voices': 'model_mt_cd_voices_ss',
    'model-mt-fg': 'model_mt_fg_b',
    'model-mt-fg-voices': 'model_mt_fg_voices_ss',
    'model-mt-fg-periodic': 'model_mt_fg_periodic_b',
    'model-mt-fg-strict': 'model_mt_fg_strict_b',
    'model-mt-fg-flexed': 'model_mt_fg_flexed_b',
    'model-mt-fg-sequential': 'model_mt_fg_sequential_b',
    'model-mt-fg-inverted': 'model_mt_fg_inverted_b',
    'model-mt-fg-retrograde': 'model_mt_fg_retrograde_b',
    'model-mt-fg-int': 'model_mt_fg_int_s',
    'model-mt-fg-tint': 'model_mt_fg_tint_s',
    'model-mt-id': 'model_mt_id_b',
    'model-mt-id-voices': 'model_mt_id_voices_ss',
    'model-mt-id-strict': 'model_mt_id_strict_b',
    'model-mt-id-flexed': 'model_mt_id_flexed_b',
    'model-mt-id-flt': 'model_mt_id_flt_b',
    'model-mt-id-invertible': 'model_mt_id_invertible_b',
    'model-mt-id-int': 'model_mt_id_int_s',
    'model-mt-id-tint': 'model_mt_id_tint_s',
    'model-mt-pe': 'model_mt_pe_b',
    'model-mt-pe-voices': 'model_mt_pe_voices_ss',
    'model-mt-pe-strict': 'model_mt_pe_strict_b',
    'model-mt-pe-flexed': 'model_mt_pe_flexed_b',
    'model-mt-pe-flt': 'model_mt_pe_flt_b',
    'model-mt-pe-sequential': 'model_mt_pe_sequential_b',
    'model-mt-pe-added': 'model_mt_pe_added_b',
    'model-mt-pe-invertible': 'model_mt_pe_invertible_b',
    'model-mt-pe-int': 'model_mt_pe_int_s',
    'model-mt-pe-tint': 'model_mt_pe_tint_s',
    'model-mt-nid': 'model_mt_nid_b',
    'model-mt-nid-voices': 'model_mt_nid_voices_ss',
    'model-mt-nid-strict': 'model_mt_nid_strict_b',
    'model-mt-nid-flexed': 'model_mt_nid_flexed_b',
    'model-mt-nid-flt': 'model_mt_nid_flt_b',
    'model-mt-nid-sequential': 'model_mt_nid_sequential_b',
    'model-mt-nid-invertible': 'model_mt_nid_invertible_b',
    'model-mt-nid-int': 'model_mt_nid_int_s',
    'model-mt-nid-tint': 'model_mt_nid_tint_s',
    'model-mt-hr': 'model_mt_hr_b',
    'model-mt-hr-voices': 'model_mt_hr_voices_ss',
    'model-mt-hr-simple': 'model_mt_hr_simple_b',
    'model-mt-hr-staggered': 'model_mt_hr_staggered_b',
    'model-mt-hr-sequential': 'model_mt_hr_sequential_b',
    'model-mt-hr-fauxbourdon': 'model_mt_hr_fauxbourdon_b',
    'model-mt-cad': 'model_mt_cad_b',
    'model-mt-cad-cantizans': 'model_mt_cad_cantizans_s',
    'model-mt-cad-tenorizans': 'model_mt_cad_tenorizans_s',
    'model-mt-cad-authentic': 'model_mt_cad_authentic_b',
    'model-mt-cad-phrygian': 'model_mt_cad_phrygian_b',
    'model-mt-cad-plagal': 'model_mt_cad_plagal_b',
    'model-mt-cad-tone': 'model_mt_cad_tone_s',
    'model-mt-cad-dtv': 'model_mt_cad_dtv_s',
    'model-mt-cad-dti': 'model_mt_cad_dti_s',
    'model-mt-int': 'model_mt_int_b',
    'model-mt-int-voices': 'model_mt_int_voices_ss',
    'model-mt-int-p6': 'model_mt_int_p6_b',
    'model-mt-int-p3': 'model_mt_int_p3_b',
    'model-mt-int-c35': 'model_mt_int_c35_b',
    'model-mt-int-c83': 'model_mt_int_c83_b',
    'model-mt-int-c65': 'model_mt_int_c65_b',
    'model-mt-fp': 'model_mt_fp_b',
    'model-mt-fp-comment': 'model_mt_fp_comment_t',
    'model-mt-fp-ir': 'model_mt_fp_ir_b',
    'model-mt-fp-range': 'model_mt_fp_range_s',
    'model-remarks': 'model_remarks_t',
    'model-created': 'model_created_dt',
    'model-updated': 'model_updated_dt',
    'model-status': 'model_status_b',
    'model-piece-id': 'model_piece_id_s',
    'model-title': 'model_title_s',
    'model-mass': 'model_mass_s',
    'model-composer': 'model_composer_s',
    'model-genre': 'model_genre_s',
    'model-date': 'model_date_i',
    'model-pdf-links': 'model_pdf_links_ss',
    'model-mei-links': 'model_mei_links_ss',
    'model-remarks': 'model_remarks_t',
    'derivative-observer': 'derivative_observer_s',
    'derivative-ema': 'derivative_ema_s',
    'derivative-mt-cf': 'derivative_mt_cf_b',
    'derivative-mt-cf-voices': 'derivative_mt_cf_voices_ss',
    'derivative-mt-cf-dur': 'derivative_mt_cf_dur_b',
    'derivative-mt-cf-mel': 'derivative_mt_cf_mel_b',
    'derivative-mt-sog': 'derivative_mt_sog_b',
    'derivative-mt-sog-voices': 'derivative_mt_sog_voices_ss',
    'derivative-mt-sog-dur': 'derivative_mt_sog_dur_b',
    'derivative-mt-sog-mel': 'derivative_mt_sog_mel_b',
    'derivative-mt-sog-ostinato': 'derivative_mt_sog_ostinato_b',
    'derivative-mt-sog-periodic': 'derivative_mt_sog_periodic_b',
    'derivative-mt-csog': 'derivative_mt_csog_b',
    'derivative-mt-csog-voices': 'derivative_mt_csog_voices_ss',
    'derivative-mt-csog-dur': 'derivative_mt_csog_dur_b',
    'derivative-mt-csog-mel': 'derivative_mt_csog_mel_b',
    'derivative-mt-cd': 'derivative_mt_cd_b',
    'derivative-mt-cd-voices': 'derivative_mt_cd_voices_ss',
    'derivative-mt-fg': 'derivative_mt_fg_b',
    'derivative-mt-fg-voices': 'derivative_mt_fg_voices_ss',
    'derivative-mt-fg-periodic': 'derivative_mt_fg_periodic_b',
    'derivative-mt-fg-strict': 'derivative_mt_fg_strict_b',
    'derivative-mt-fg-flexed': 'derivative_mt_fg_flexed_b',
    'derivative-mt-fg-sequential': 'derivative_mt_fg_sequential_b',
    'derivative-mt-fg-inverted': 'derivative_mt_fg_inverted_b',
    'derivative-mt-fg-retrograde': 'derivative_mt_fg_retrograde_b',
    'derivative-mt-fg-int': 'derivative_mt_fg_int_s',
    'derivative-mt-fg-tint': 'derivative_mt_fg_tint_s',
    'derivative-mt-id': 'derivative_mt_id_b',
    'derivative-mt-id-voices': 'derivative_mt_id_voices_ss',
    'derivative-mt-id-strict': 'derivative_mt_id_strict_b',
    'derivative-mt-id-flexed': 'derivative_mt_id_flexed_b',
    'derivative-mt-id-flt': 'derivative_mt_id_flt_b',
    'derivative-mt-id-invertible': 'derivative_mt_id_invertible_b',
    'derivative-mt-id-int': 'derivative_mt_id_int_s',
    'derivative-mt-id-tint': 'derivative_mt_id_tint_s',
    'derivative-mt-pe': 'derivative_mt_pe_b',
    'derivative-mt-pe-voices': 'derivative_mt_pe_voices_ss',
    'derivative-mt-pe-strict': 'derivative_mt_pe_strict_b',
    'derivative-mt-pe-flexed': 'derivative_mt_pe_flexed_b',
    'derivative-mt-pe-flt': 'derivative_mt_pe_flt_b',
    'derivative-mt-pe-sequential': 'derivative_mt_pe_sequential_b',
    'derivative-mt-pe-added': 'derivative_mt_pe_added_b',
    'derivative-mt-pe-invertible': 'derivative_mt_pe_invertible_b',
    'derivative-mt-pe-int': 'derivative_mt_pe_int_s',
    'derivative-mt-pe-tint': 'derivative_mt_pe_tint_s',
    'derivative-mt-nid': 'derivative_mt_nid_b',
    'derivative-mt-nid-voices': 'derivative_mt_nid_voices_ss',
    'derivative-mt-nid-strict': 'derivative_mt_nid_strict_b',
    'derivative-mt-nid-flexed': 'derivative_mt_nid_flexed_b',
    'derivative-mt-nid-flt': 'derivative_mt_nid_flt_b',
    'derivative-mt-nid-sequential': 'derivative_mt_nid_sequential_b',
    'derivative-mt-nid-invertible': 'derivative_mt_nid_invertible_b',
    'derivative-mt-nid-int': 'derivative_mt_nid_int_s',
    'derivative-mt-nid-tint': 'derivative_mt_nid_tint_s',
    'derivative-mt-hr': 'derivative_mt_hr_b',
    'derivative-mt-hr-voices': 'derivative_mt_hr_voices_ss',
    'derivative-mt-hr-simple': 'derivative_mt_hr_simple_b',
    'derivative-mt-hr-staggered': 'derivative_mt_hr_staggered_b',
    'derivative-mt-hr-sequential': 'derivative_mt_hr_sequential_b',
    'derivative-mt-hr-fauxbourdon': 'derivative_mt_hr_fauxbourdon_b',
    'derivative-mt-cad': 'derivative_mt_cad_b',
    'derivative-mt-cad-cantizans': 'derivative_mt_cad_cantizans_s',
    'derivative-mt-cad-tenorizans': 'derivative_mt_cad_tenorizans_s',
    'derivative-mt-cad-authentic': 'derivative_mt_cad_authentic_b',
    'derivative-mt-cad-phrygian': 'derivative_mt_cad_phrygian_b',
    'derivative-mt-cad-plagal': 'derivative_mt_cad_plagal_b',
    'derivative-mt-cad-tone': 'derivative_mt_cad_tone_s',
    'derivative-mt-cad-dtv': 'derivative_mt_cad_dtv_s',
    'derivative-mt-cad-dti': 'derivative_mt_cad_dti_s',
    'derivative-mt-int': 'derivative_mt_int_b',
    'derivative-mt-int-voices': 'derivative_mt_int_voices_ss',
    'derivative-mt-int-p6': 'derivative_mt_int_p6_b',
    'derivative-mt-int-p3': 'derivative_mt_int_p3_b',
    'derivative-mt-int-c35': 'derivative_mt_int_c35_b',
    'derivative-mt-int-c83': 'derivative_mt_int_c83_b',
    'derivative-mt-int-c65': 'derivative_mt_int_c65_b',
    'derivative-mt-fp': 'derivative_mt_fp_b',
    'derivative-mt-fp-comment': 'derivative_mt_fp_comment_t',
    'derivative-mt-fp-ir': 'derivative_mt_fp_ir_b',
    'derivative-mt-fp-range': 'derivative_mt_fp_range_s',
    'derivative-remarks': 'derivative_remarks_t',
    'derivative-created': 'derivative_created_dt',
    'derivative-updated': 'derivative_updated_dt',
    'derivative-status': 'derivative_status_b',
    'derivative-piece-id': 'derivative_piece_id_s',
    'derivative-title': 'derivative_title_s',
    'derivative-mass': 'derivative_mass_s',
    'derivative-composer': 'derivative_composer_s',
    'derivative-genre': 'derivative_genre_s',
    'derivative-date': 'derivative_date_i',
    'derivative-pdf-links': 'derivative_pdf_links_ss',
    'derivative-mei-links': 'derivative_mei_links_ss',
    'derivative-remarks': 'derivative_remarks_t',
}
