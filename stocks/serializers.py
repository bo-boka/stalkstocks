# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        # fields =('ticker', 'volume')
        fields = '__all__'