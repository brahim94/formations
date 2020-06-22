# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RhPlusAxeFormation(models.Model):

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

class RhPlusFormation(models.Model):

    _name = 'rh_plus.formation'
    
    name = fields.Char('Fromation')
    #axe_id = fields.Many2one('rh_plus.planning', string="Axe ID")

class RhPlusDemandeFormation(models.Model):

    _name = 'rh_plus.demande_formation'
    
    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    employee_id = fields.Many2one('hr.employee', string="Demandeur")
    state = fields.Selection([
        ('new', 'Nouvelle'),
        ('valide', 'Validé'),
        ('done', 'Faite'),
        ], setting='State', readonly=True, default='new')
    date_request = fields.Datetime('Date demande')
    fiche_poste = fields.Many2one('hr.job', string='Poste')
    service = fields.Many2one('hr.department', string='Service')
    type_request = fields.Selection([
            ('indiv', 'Individuelle'),
            ('collec', 'Collective'),
            ], setting='Type', default='indiv', required=True)
    nature_request = fields.Selection([
            ('prev', 'Prévu'),
            ('imprev', 'Non Prévu'),
            ], setting='Nature', default='prev', required=True)
    mode_request = fields.Selection([
            ('elearning', 'E-leraning'),
            ('intern', 'Interne'),
            ('extern', 'Externe : National'),
            ('externinter', 'Extern : Internation'),
            ], setting='Mode', default='elearning', required=True)
    priority = fields.Integer('Priorité')
    date_begin = fields.Date('Date début')
    date_end = fields.Date('Date limite')
    planing_id = fields.Many2one('rh_plus.planning', string="Plan previsionel")
    axe_formation_id = fields.Many2one('rh_plus.axe_formation', string="Axe de formation")
    formation_id = fields.Many2one('rh_plus.formation', string="Formation")
    diplomated = fields.Boolean('diplômante ?')
    duration = fields.Float('Durée')
    absence_duration = fields.Float("Durée d'abscence")
    duration_unit = fields.Selection([
            ('hours', 'Heures'),
            ('weeks', 'Semaines'),
            ('mounths', 'Mois'),
            ('year', 'Ans'),
            ], setting='Mode', default='hours', required=True)
    absece_duration_unit = fields.Selection([
            ('hours', 'Heures'),
            ('weeks', 'Semaines'),
            ('mounths', 'Mois'),
            ('year', 'Ans'),
            ], setting='Mode', default='hours', required=True)
    financial_type = fields.Selection([
            ('intern', 'Interne'),
            ('extern', 'Externe'),
            ('other', 'Autre'),
            ], setting='Type de financement', default='intern', required=True)
    financial_item = fields.Float('Taux de financement')
    etablissment_cordination = fields.Text('Etablissement et coordonnées')
    etablissment_location = fields.Text("Lieu d'etablissement")
    objectif_wanted = fields.Text('Objetif vises')
    result_wanted = fields.Text('Resultats attendus')
    themat = fields.Text('Thématique scientifique /métier support')
    themat_reference = fields.Text('Thème de référence')


    @api.onchange('employee_id')
    def onchange_employee_id(self):
        self.fiche_poste = self.employee_id.job_id
        self.service = self.employee_id.department_id
    
    @api.model 
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('formation.order') or ('New')
        result = super(RhPlusDemandeFormation, self).create(vals)
        return result 

class RhPlusDemandeEncoursFormation(models.Model):

    _name = 'rh_plus.encours_formation'
    
    name = fields.Char('fromation en cours')

class RhPlusanalyticFormation(models.Model):

    _name = 'rh_plus.analyse_formation'
    
    name = fields.Char('nom')
