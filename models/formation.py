# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RhPlusFormation(models.Model):

    _name = 'rh_plus.axe_formation'
    
    name = fields.Char('Axe de fromation')
    axe_id = fields.Many2one('rh_plus.planning', string="Axe ID")

class RhPlusPlaning(models.Model):

    _name = 'rh_plus.planning'
    
    date_begin = fields.Date('Date début')
    date_end = fields.Date('Date fin')
    estimated_budget = fields.Float('Budget prévisionnel')
    mode_plan = fields.Selection([
            ('indiv', 'Individuelle'),
            ('collec', 'Collective'),
            ], setting='Mode', default='indiv', required=True)
    year = fields.Integer('Année')
    obligated = fields.Boolean('Obligatoir ?')
    formationaxe_id = fields.One2many('rh_plus.axe_formation','axe_id', string='Axe de formation')

