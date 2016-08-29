from openerp import models, fields, api
from openerp import _
import logging
_logger = logging.getLogger(__name__)


class AccountAssetAsset(models.Model):
    _inherit = 'account.asset.asset'

    account_analytic_id = fields.Many2one('account.analytic.account', string='Analytic account')

    def onchange_category_id(self, cr, uid, ids, category_id, context=None):
        context = context or {}
        val = super(AccountAssetAsset, self).onchange_category_id(cr, uid, ids, category_id, context=context)
        val = val or {'value': {}}
        if category_id:
            category = self.pool.get('account.asset.category').browse(cr, uid, category_id, context=context)
            if category.account_analytic_id:
                val['value']['account_analytic_id'] = category.account_analytic_id.id
        return val

class AccountAssetDepreciationLine(models.Model):
    _inherit = 'account.asset.depreciation.line'

    def create_move(self, cr, uid, ids, context=None):
        context = context or {}
        created_move_ids = super(AccountAssetDepreciationLine, self).create_move(cr, uid, ids, context=None)
        if not created_move_ids:
            return created_move_ids
        move_line_obj = self.pool.get('account.move.line')
        for line in self.browse(cr, uid, ids, context=context):
            aml_ids = move_line_obj.search(cr, uid, [('asset_id', '=', line.asset_id), ('move_id', 'in', created_move_ids), ('debit', '>', 0)], context=context)
            if aml_ids and line.asset_id.account_analytic_id:
                move_line_obj.write(cr, uid, aml_ids, {
                    'analytic_account_id': line.asset_id.account_analytic_id.id,
                }, context=context)
        return created_move_ids
