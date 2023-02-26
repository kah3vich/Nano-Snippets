import * as vscode from 'vscode';
import { consoleLog } from './utils/other';

export const activate = (context: vscode.ExtensionContext) => {
	const disposable = vscode.commands.registerCommand('nano-snippets', function () {
		consoleLog('Nano Snippets', 'log');

		context.subscriptions.push(disposable);
	});
};

export const deactivate = () => {};
export { consoleLog };
